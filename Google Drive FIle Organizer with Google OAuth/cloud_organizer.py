import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import PySimpleGUI as sg
import tkinter as tk
from tkinter import messagebox
import os
import sys

def find_client_json():
    # Get the directory of the current Python script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Search for client.json in the current directory
    for file_name in os.listdir(current_dir):
        if file_name == 'client_secret.json':
            return os.path.join(current_dir, file_name)

    # If client.json is not found, return None
    return None

# Example usage
if __name__ == "__main__":
    client_json_path = find_client_json()
    if client_json_path:
        print("client.json found at:", client_json_path)
    else:
        print("client.json not found in the same directory as the script.")



# Autenticador Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']

# Caminho do arquivo com as chaves do cliente OAuth 2.0
CLIENT_SECRET_FILE = client_json_path

# Arquivo Token para acessar a API do Google
TOKEN_FILE = 'token.json'

# ID da pasta do Google Drive (É localizado no url da pasta)
DRIVE_FOLDER_ID = '1fdFRdBgpvJTn5oATfQqgkDpw9xBhWvKf'

# Função autenticadora de usuário.
# Para funcionar o usuário deve estar inscrito como cliente no Google Cloud Services ...
# e ter suas próprias credencias. (Para mais informações ler readme.txt)


def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)

    with open(TOKEN_FILE, 'w') as token:
        token.write(credentials.to_json())

    return credentials


# Faz o upload dos arquivos do diretório local em uma nova pasta.
def upload_folder(service, local_folder_path, parent_folder_id):

    folder_metadata = {
        'name': os.path.basename(local_folder_path),
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id]
    }

    new_folder = service.files().create(body=folder_metadata).execute()
    new_folder_id = new_folder['id']

    for root, dirs, files in os.walk(local_folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            media = service.files().create(
                body={'name': file_name, 'parents': [new_folder_id]},
                media_body=file_path,
                fields='id'
            ).execute()

            print(
                f'Upload do arquivo: {file_name} concluído. ID: {media["id"]}')
            
    new_path = f'https://drive.google.com/drive/u/1/folders/{new_folder_id}'
    print(
        f'O upload do diretório está concluído.',
        'ID da nova pasta:',
        new_path,
        sep='\n')
    
    root = tk.Tk()
    root.withdraw()  
    messagebox.showinfo("Upload concluído.", f"Confira a pasta no Google Driven {new_path}")


# Analisa as credenciais 
def main(folder_path):
    credentials = None

    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE)

    if not credentials or not credentials.valid:
        credentials = authenticate()

    service = build('drive', 'v3', credentials=credentials)

    local_folder_path = folder_path
    upload_folder(service, local_folder_path, DRIVE_FOLDER_ID)

# Cria a interface para escolha do diretório
def interface():

    layout = [
        [sg.Text("Selecione a pasta para o upload:")],
        [sg.InputText(key="-FOLDER-"), sg.FolderBrowse()],
        [sg.Button("Enviar")]
    ]

    window = sg.Window("Exportação para Google Drive", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Enviar":
            selected_directory = values["-FOLDER-"]

            sg.popup(
                f"Diretório escolhido: {selected_directory}", title="Diretório")

            window.close()

    return selected_directory



if __name__ == '__main__':
    main(interface())
