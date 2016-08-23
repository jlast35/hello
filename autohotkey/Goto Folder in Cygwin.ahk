#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
;-------------------------------------------------------------------------------
; Opens Cygwin command prompt at current folder in Windows Explorer.
; Assumes you have open Windows Explorer window in focus that you have navigated to the folder you want to open in Cygwin.
; PRE: You have not hidden the address bar.
; <Alt + C> in Windows Explorer to execute this script.
#IfWinActive ahk_class CabinetWClass ; Only applies to Explorer windows.
$!c::
    saved := ClipboardAll
    ; Go to address bar and select path there.
    ;Send ^l ;this will only work in Windows 8, whereas <Alt + D> will work in both Windows 7 and 8
	Send ^l
    Sleep 10
    ; Copy the path.
    Send ^c
    Sleep 10
    ClipWait, 2
    if ErrorLevel {
        MsgBox, The attempt to copy text onto the clipboard failed.
        return
    } ; if

    ; Run Cygwin.
    Run, C:\cygwin64\bin\mintty.exe -i /Cygwin-Terminal.ico -
    WinWait, ~
    WinActivate, ~
    WinMaximize, ~
    ; Go to the path from Windows Explorer.
    ; Have to use cygpath to translate Windows path into a Cygwin path.
    Send cd "$(cygpath '%clipboard%')"{Enter} ;added quotes due to some Windows folders having spaces
    
    ; Restore clipboard.
    Clipboard := saved
    saved =
return
#IfWinActive
