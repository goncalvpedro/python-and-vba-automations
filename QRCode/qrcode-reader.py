import tkinter as tk
from tkinter import messagebox
import pandas as pd
import time, os, subprocess
from datetime import datetime

class DataEntryApp:

    ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    markers = {
        '5': ' 2005',
        '6': ' 2006',
        '7': ' 2007',
        '8': ' 2008',
    }

    def __init__(self, window):
        self.window = window
        self.window.title("Double Check Gravação")
        self.window.geometry("280x330")

        self.data_frame = pd.DataFrame(columns=['Value', 'PN cliente', 'Cliente', 'Gravadora', 'Sequencial', 'Data'])

        self.entry_label = tk.Label(window, text="QR CODE")
        self.entry_label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(window, width=25)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        self.entry.bind("<Return>", self.submit_data)

        self.last_10_label = tk.Label(window, text="Últimas 10 leituras: ")
        self.last_10_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.last_10_text = tk.Text(window, height=10, width=30)
        self.last_10_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.close_day_button = tk.Button(window, text="Enviar leituras", command=self.send_data)
        self.close_day_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.close_day_button = tk.Button(window, text="Encerrar dia", command=self.close_day)
        self.close_day_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def submit_data(self, event=None):
        value = self.entry.get()

        if value.strip() != '':
            new_row = {'Value': value, 'PN cliente': str(value)[0:11],
                       'Cliente': str(value)[11:16],
                       'Gravadora': str(value)[16:17],
                       'Sequencial': str(value)[17:21],
                       'Data': str(value)[21:]
            }
            
        self.data_frame = pd.concat([self.data_frame, pd.DataFrame([new_row])], ignore_index=True)
        self.data_frame['Gravadora'] = self.data_frame['Gravadora'].map(self.markers)
        self.entry.delete(0, 'end')
        self.update_last_10_values()

        return self.data_frame

    def update_last_10_values(self):
        last_10_values = self.data_frame['Value'].tail(10).tolist()
        self.last_10_text.delete(1.0, 'end')
        for value in last_10_values:
            self.last_10_text.insert('end', f"{value}\n")

    def send_data(self):
        leituras_folder = os.path.join(self.ROOT_FOLDER, 'Leituras')
        if not os.path.exists(leituras_folder):
            os.makedirs(leituras_folder)
        
        if self.data_frame.empty:
            return
        else: 
            today = datetime.now().strftime('%Y_%m_%d_%H_%M')
            file_path = os.path.join(leituras_folder, f'{today}_double_check.csv')
            self.data_frame.to_csv(file_path, index=False)
     
    def send_data_to_db(self):
        if self.new_row.empty:
            return
        else: 
            self.insert_into_db(self.new_row)

    def close_day(self):
        result = messagebox.askyesno("Encerrar dia", "Deseje confirmar o encerramento? ")

        if result:
            messagebox.showinfo("Encerramento confirmado", "O computador irá desligar em 30 segundos.")
            self.send_data()
            self.window.destroy()
            time.sleep(30)
            if os.name == 'nt':
                subprocess.call(['shutdown', '/s', '/t', '1'])
            else:
                subprocess.call(['shutdown', '-h', 'now'])
        else:
            return

def main():
    root = tk.Tk()
    app = DataEntryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()