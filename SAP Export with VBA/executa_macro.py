
import win32com.client
from tkinter import Tk, messagebox
import time


def execute_vba_code(file_path, module_name, procedure_name):

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True

    # Initialize workbook to None
    workbook = None  

    try:
        # Open the Excel workbook
        workbook = excel.Workbooks.Open(file_path)

        # Access the VBA project in the workbook
        vba_project = workbook.VBProject

        # Access the module containing the VBA code
        vba_module = vba_project.VBComponents(module_name).CodeModule

        # Execute the specified procedure in the VBA code
        excel.Run(f"{module_name}.{procedure_name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:

        if workbook is not None:
            # Close the workbook only if it has been opened
            workbook.Close(SaveChanges=False)
        excel.Quit()


# Example usage
file_path = r"Excel file path"
module_name = "Change this to the name of your VBA module"
procedure_name = "Sub name"

execute_vba_code(file_path, module_name, procedure_name)

root = Tk()
root.withdraw()
messagebox.showinfo("| Updated. |",
                    "  Closing. ")
