import win32com.client
import time

def Conexao_SAP(Transaction):
    try:
        Session = None
        SapGui = None
        Appl = None
        WshShell = None
        proc = None

        try:
            Session = win32com.client.GetObject("SAPGUI").GetScriptingEngine.Children(0).Children(0)
        except:
            pass

        if Session is None:
            WshShell = win32com.client.Dispatch("WScript.Shell")

            # Paste your saplogon.exe string here. However this path is very common and might be same as yours either.
            proc = WshShell.Exec(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe") 
            time.sleep(5)
            SapGui = win32com.client.GetObject("SAPGUI")
            Appl = SapGui.GetScriptingEngine
            Connection = Appl.OpenConnection("Name of your connection here - exactly as in SAP", True)
            Session = Connection.Children(0)

        ApplicationSAP = None
        try:
            ApplicationSAP = win32com.client.GetObject("SAPGUI").GetScriptingEngine
        except:
            pass

        if ApplicationSAP is None:
            SapGuiAuto = win32com.client.GetObject("SAPGUI")
            ApplicationSAP = SapGuiAuto.GetScriptingEngine

        Session.findById("wnd[0]/tbar[0]/okcd").Text = "/n"
        Session.findById("wnd[0]").sendVKey(0)
        Session.findById("wnd[0]/tbar[0]/okcd").Text = Transaction
        Session.findById("wnd[0]").sendVKey(0)

    except Exception as e:
        print("Error:", e)

def vl10e():
    # Paste the SAP script of your automation. 
    # https://help.sap.com/docs/sap_gui_for_windows/b47d018c3b9b45e897faf66a6c0885a8/babdf65f4d0a4bd8b40f5ff132cb12fa.html?version=760.00&locale=en-US
    # https://youtu.be/ISDX5LwcVPQ?si=TQYbKniu1dx1EhK4
    pass
# Example usage:
if __name__ == "__main__":
    Transaction = ""
    Conexao_SAP(Transaction)
