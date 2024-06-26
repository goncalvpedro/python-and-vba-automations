' You can copy this script in a module in Excel to open SAP logon using a macro
Public Session

Sub Conexao_SAP(ByVal transaction As String)



    Dim Connection, SapGui, Appl, WshShell, proc
    
    On Error GoTo DESLOGADO
        Set Session = GetObject("SAPGUI").GetScriptingEngine.Children(0).Children(0)
    GoTo LOGADO
    
DESLOGADO:

    Set WshShell = CreateObject("WScript.Shell")

    Set proc = WshShell.Exec("Path to saplogon.exe file") 'Usually found in "C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
       
    Application.Wait Now + TimeValue("0:00:5")
   
    Set SapGui = GetObject("SAPGUI")
    
    Set Appl = SapGui.GetScriptingEngine
  
    Set Connection = Appl.OpenConnection("Connection name", True) ' Same as in SAP
   
    Set Session = Connection.Children(0)
    
LOGADO:
    On Error GoTo -1
         
  Application.DisplayAlerts = False
   On Error Resume Next
   If Not IsObject(ApplicationSAP) Then
      On Error Resume Next
      Set SapGuiAuto = GetObject("SAPGUI")
      If Err Then MsgBox ("SAP System - Not found...!")
         Set ApplicationSAP = SapGuiAuto.GetScriptingEngine
      If Err Then MsgBox ("SAP System - Cancelled...!")
   End If
     
   With Session
      .findById("wnd[0]/tbar[0]/okcd").Text = "/n"
      .findById("wnd[0]").sendVKey 0
      .findById("wnd[0]/tbar[0]/okcd").Text = transaction
      .findById("wnd[0]").sendVKey 0
   End With

End Sub

