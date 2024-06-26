Option Explicit
Sub updateData()

    ' Close other workbooks
    Dim wb As Workbook
    
    For Each wb In Workbooks
    
        If wb.Name <> ThisWorkbook.Name Then
        
            wb.Close SaveChanges:=True
        
        End If
        
    Next wb

    ' Call your Sub containing the transaction script
    Call updateTransaction
    
    
    Application.Wait Now + TimeValue("00:00:05")

    ' Update workbooks
    
    ActiveWorkbook.RefreshAll
    
    MsgBox "Finished", vbInformation + vbModeless
    
End Sub
