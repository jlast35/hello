#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

WaitForWebsite()
{
	PixelGetColor, color, 275, 155
	previous_color := color
	While color != 0x0000FF
	{
		PixelGetColor, color, 275, 155
	}
	Sleep 50
	MsgBox The color at the 275, 155 is %color%.
}
return

^+x::
WaitForWebsite()
return
