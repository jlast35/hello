#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
; -------------------------------------------------------------------------------------------
FileEncoding UTF-8 ;this is so that synopses with foreign text display properly instead of with garbled symbols representing foreign characters

EnvGet, user, USERPROFILE ;we need to get this path variable because dropbox is relative to the home path for each user, and AHK has issues with %USERPROFILE% due to the percent signs
textPath := user . "\Dropbox\Content Share\Library-Text_ready\movies\eng\"
imagePath := user . "\Dropbox\Content Share\Library-Graphics_ready\movies\"
playerBackground := user . "\Dropbox\Content Share\anthonysmenu\Menuing\ana_l72\menu\images\bg-a1.png"
iconPath := user . "\Dropbox\Content Share\anthonysmenu\Menuing\ana_l72\menu\images\icons\"

filelist := [] ;don't forget to use := to assign the empty array. if you use = then it will assign the literal text [] to the variable filelist
Loop, % textPath . "*.txt"
	filelist.Insert(A_LoopFileName) ;looks like I can get the absolute path name of each file

current := 1 ;this is the array index that gets modified by the previous and next buttons to display a given filename
FileRead synopsis, % textPath . filelist[current] ;the synopsis variable is initialized here
imageFile := imagePath . RegExReplace(filelist[current], "\.txt", ".png")

Gui, Add, Picture, x0 y0, % playerBackground
Gui, Add, Picture, x2 y2 BackgroundTrans Section, % iconPath . "icon-tb-back.png"
Gui, Add, Picture, x714 y2 BackgroundTrans Section, % iconPath . "icon-tb-home.png"
Gui, Add, Picture, x754 y2 BackgroundTrans Section, % iconPath . "icon-tb-settings.png"
Gui, Font, s11
Gui, Add, Text, x50 y12 BackgroundTrans, Movies
Gui, Add, Picture, Section x10 y185 vButtonPrev gButtonPrev BackgroundTrans, % iconPath . "chevron_lg_left.png" ;if I assign a handler to g... I can label the button something different from the subroutine it calls
Gui, Add, Picture, vMoviePoster ys-85 Section w193 h290, % imageFile
Gui, Add, Text, vSynopsisText ys w470 h290 BackgroundTrans Border, % synopsis ;if I assign the control a variable using v... I can reference the control later to update it
Gui, Add, Picture, ys+85 vButtonNext gButtonNext BackgroundTrans, % iconPath . "chevron_lg_right.png" ;this Section and ys stuff is to make the two buttons show on the same row on the Gui
Gui, Add, Button, x268 y417 w100, Play
Gui, Show, , L7 Player Simulation ;this is how you set the window title for the GUI and make the GUI visible
Return

GuiClose: ;this automatically gets called when you hit the X (close) button on the Gui window 
ExitApp

ButtonPrev:
if (current > 1)
{
	current -= 1
	Gosub UpdateGui 
}
Return

ButtonNext:
if (current < filelist.MaxIndex())
{
	current += 1
	Gosub UpdateGui
}
Return

UpdateGui:
GuiControl, , MyText, % RegExReplace(filelist[current], "\.txt", "") ;text control does not auto-resize to fit new text
FileRead synopsis, % textPath . filelist[current] ;unicode text will not display properly if you don't have FileEncoding UTF-8 set
GuiControl, , SynopsisText, % synopsis
imageFile := imagePath . RegExReplace(filelist[current], "\.txt", ".png")
GuiControl, , MoviePoster, % imageFile
if (current == 1)
	GuiControl, Hide, ButtonPrev
else
	GuiControl, Show, ButtonPrev
if (current == filelist.MaxIndex())
	GuiControl, Hide, ButtonNext
else
	GuiControl, Show, ButtonNext
	
Return
