import tkinter as tk
from tkinter import filedialog

def select_files():
    file_paths = filedialog.askopenfilenames()
    return file_paths

def get_file_info():
    files = select_files()
    file_list = []
    
    for file in files:
        file_name = file.split('/')[-1].split('.')[0]
        info = (file, file_name)
        file_list.append(info)
    
    return file_list

root = tk.Tk()
root.withdraw()
