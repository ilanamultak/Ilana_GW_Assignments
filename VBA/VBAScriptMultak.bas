Attribute VB_Name = "Module1"
Sub STOCKDATA()

Dim ws As Worksheet
For Each ws In Worksheets

Dim Ticker As String
Dim i As Long
Dim YearlyChange As Long
Dim TotalStockVolume As Double
Dim PercentChange As Double
Dim closing As Double
Dim starting_open As Double
Dim volume As Double

ws.Range("I1").Value = "Ticker"
ws.Range("J1").Value = "Yearly Change"
ws.Range("K1").Value = "Percent Change"
ws.Range("L1").Value = "Total Stock Volume"

Start = 2
summary_row = 2

RowCount = ws.Range("A1").End(xlDown).Row

For i = 2 To RowCount

starting_open = ws.Cells(Start, 3)
closing = ws.Cells(i, 6).Value
volume = ws.Cells(i, 7).Value

    If ws.Cells(i, 1).Value = ws.Cells(i + 1, 1).Value Then
    Total = Total + volume
    Else
    Total = Total + volume
    
    Change = (closing - starting_open)
    
        If starting_open = 0 Then
        PercentChange = 0
        Else
        PercentChange = (Change / starting_open)
        End If
    
    PercentChange = (Change / starting_open)

    Start = i + 1
    
    ws.Range("I" & summary_row).Value = ws.Cells(i, 1).Value
    ws.Range("J" & summary_row).Value = Round(Change, 2)
    ws.Range("K" & summary_row).Value = PercentChange
    ws.Range("L" & summary_row).Value = Total
    
    Range("K" & summary_row).NumberFormat = "0.00%"
    
        Total = 0
        Change = 0
        summary_row = summary_row + 1
        End If
    
    If (Total > 0) Then
    ws.Range("L" & summary_row).Value = closing - starting_open
    End If
    
    If ws.Range("J" & summary_row).Value > 0 Then
    ws.Range("J" & summary_row).Interior.ColorIndex = 4
    Else
    ws.Range("J" & summary_row).Interior.ColorIndex = 3
    End If
    
Next i

Next ws

End Sub
