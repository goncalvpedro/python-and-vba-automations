' Here is a example on how export the transaction "VL10E" usually used for supply chain 

Sub updateTransaction()

    Call Conexao_SAP("VL10E")
    
Dim Appl

' The worksheet containing the parameters if they're dinamic. If they are static just create variables for them.

Dim sheetName As String
sheetName = "" 

Dim ws As Worksheet
Set ws = Worksheets(sheetName)


' Variables
Dim center, filename, filepath As String
Dim date1, date2 As Variant

' Indicação da células que contém os parâmetros
center = ws.Range("cell")
date1 = ws.Range("cell").Text
date2 = ws.Range("cell").Text
filename = ws.Range("cell").Text
filepath = ws.Range("cell").Text

' This following script you can find using "Record or register script" something like that.
' Copy the code that SAP will generate and paste here

Session.findById("wnd[0]").maximize
Session.findById("wnd[0]").sendVKey 0
Session.findById("wnd[0]/usr/ctxtST_VSTEL-LOW").Text = center
Session.findById("wnd[0]/usr/ctxtST_LEDAT-LOW").Text = Replace(date1, "/", ".")
Session.findById("wnd[0]/usr/ctxtST_LEDAT-HIGH").Text = Replace(date2, "/", ".")
Session.findById("wnd[0]/usr/ctxtST_LEDAT-HIGH").SetFocus
Session.findById("wnd[0]/usr/ctxtST_LEDAT-HIGH").caretPosition = 10
Session.findById("wnd[0]/tbar[1]/btn[8]").press
Session.findById("wnd[0]/tbar[1]/btn[46]").press
Session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[2]").Select
Session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").Select
Session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").SetFocus
Session.findById("wnd[1]/tbar[0]/btn[0]").press

' Add some sleep time so SAP can export the data
Application.Wait Now + TimeValue("0:0:10")

On Error Resume Next
    Session.findById("wnd[1]/usr/ctxtDY_PATH").Text = filepath
    Session.findById("wnd[1]/usr/ctxtDY_FILENAME").Text = filename
    Session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 20
    Session.findById("wnd[1]/tbar[0]/btn[11]").press
    Session.findById("wnd[0]/tbar[0]/btn[15]").press
    Session.findById("wnd[0]/tbar[0]/btn[15]").press

If Err.Number <> 0 Then
    MsgBox "Error saving the exported file, check the directory folder for .txt file"
End If
    
End Sub

