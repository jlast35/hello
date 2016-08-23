#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;if you want text with multiple sizes, since a given text box can only have one font size, you have to create a separate text box for each different sized text
fontsize := 5
Gui, Font, s%fontsize% ;demonstrating how to use variables in conjunction with the font sizing
Gui, Add, Text, , Size1`n
Gui, Font, s14
Gui, Add, Text, y+0, Size2`n ;if you use the y+0 option, you don't have to calculate font size offsets - it just places it immediately below the last line
Gui, Font, s12
Gui, Add, Text, y+0, Size3 ;even the mixed carriage return line sizes space correctly
Gui, Show
Return
