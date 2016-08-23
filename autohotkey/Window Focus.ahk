#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^+z::
IfWinExist, TopEffects Digital Content Management System - Mozilla Firefox
{
	WinActivate
	WinMove, TopEffects Digital Content Management System - Mozilla Firefox, , 1912, 172, 1456, 876
	WinMaximize, TopEffects Digital Content Management System - Mozilla Firefox
	;WinGetPos, X, Y, W, H, A  ; "A" to get the active window's pos.
	;MsgBox, The active window is at %W%`,%H%
	
}
Else
{
	Run iexplore.exe www.topeffects.com ; if you don't specify which browser to run, it uses you default browser (mine is Firefox)
	;MouseMove, 0, 0
	;WinWait TopEffects Digital Content Management System
	;StatusBarWait, Done, 30
	;if ErrorLevel
	;	MsgBox The wait timed out or the window was closed. 
	;else 
	;	MsgBox The page is done loading.
	; The above code doesn't work because there is no status bar text in Explorer or Firefox anymore for AHK to check.
	; It seems the simplest solution is just to use a Sleep command of about 4000 milliseconds - usually enough time for the page to load or transfer data
	; Even though it might not be the most efficient way, it will usually work just fine though
	WinMove, TopEffects Digital Content Management System, , 1912, 172, 1456, 876
	WinMaximize, TopEffects Digital Content Management System
}
Return
