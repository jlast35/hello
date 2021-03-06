﻿#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
; -------------------------------------------------------------------------------------------
FileEncoding UTF-8 ;this is so that synopses with foreign text display properly instead of with garbled symbols representing foreign characters

;Here we just define the paths to everything
EnvGet, user, USERPROFILE ;we need to get this path variable because dropbox is relative to the home path for each user, and AHK has issues with %USERPROFILE% due to the percent signs

;choose some arbitrary default values to start with - ANA was the initial test subject for development of this script, so it is first
AirlineChoice := "ana_l72"
MediaChoice := "movies"

Gosub StartPlayer
Return

StartPlayer:
Gosub InitializeCollateral
Gosub InitializeGui

InitializeCollateral:
textPath := user . "\Dropbox\Content Share\anthonysmenu\Menuing\" . AirlineChoice . "\menu\text\" . MediaChoice . "\eng\"
imagePath := user . "\Dropbox\Content Share\anthonysmenu\Menuing\" . AirlineChoice . "\menu\images\interface\"
playerBackground := user . "\Dropbox\Content Share\anthonysmenu\Menuing\" . AirlineChoice . "\menu\images\bg-a1.png"
iconPath := user . "\Dropbox\Content Share\anthonysmenu\Menuing\" . AirlineChoice . "\menu\images\icons\"
filelist := [] ;don't forget to use := to assign the empty array. if you use = then it will assign the literal text [] to the variable filelist
Loop, % textPath . "*.txt"
	filelist.Insert(A_LoopFileName) ;looks like I can get the absolute path name of each file
current := 1 ;this is the array index that gets modified by the previous and next buttons to display a given filename
;MsgBox % filelist[current]
Return

InitializeGui: ;this section is full of magic numbers for control placement on-screen
Gui, Add, Picture, x0 y0, % playerBackground
Gui, Add, DropDownList, x130 y10 w130 Sort gAirlineChosen vAirlineSelection, aeroflot_l72|alaska_l72|ana_l72|arkefly|azal_l72|ethiopian_l72|fijiairways|garuda_xt|gulfair_l10|Kenya_l10|NorthAmerican_L10|RAM|suncountry_l72
GuiControl, ChooseString, AirlineSelection, % AirlineChoice
Gui, Add, DropDownList, x270 y10 w60 Sort gMediaChosen vMediaSelection, movies|tv
GuiControl, ChooseString, MediaSelection, % MediaChoice
Gui, Add, Picture, x2 y2 BackgroundTrans Section, % iconPath . "icon-tb-back.png"
Gui, Add, Picture, x714 y2 BackgroundTrans Section, % iconPath . "icon-tb-home.png"
Gui, Add, Picture, x754 y2 BackgroundTrans Section, % iconPath . "icon-tb-settings.png"
Gui, Font, s13;too bad you can only apply formatting to ALL the text on a control at once... AHK just doesn't support RTF or HTML in text boxes...
Gui, Add, Text, x50 y12 BackgroundTrans cWhite, % MediaChoice
Gui, Add, Picture, Section x10 y185 vButtonPrev gButtonPrev BackgroundTrans, % iconPath . "chevron_lg_left.png" ;if I assign a handler to g... I can label the button something different from the subroutine it calls
Gui, Add, Picture, vMoviePoster ys-85 Section w165 h218, % imageFile ;apparently, the sizes of the source images are scaled down for integration - or is this just ANA?
Gui, Add, Text, vSynopsisText ys w470 h218 BackgroundTrans cWhite, % synopsis ;if I assign the control a variable using v... I can reference the control later to update it
Gui, Add, Picture, ys+85 vButtonNext gButtonNext BackgroundTrans, % iconPath . "chevron_lg_right.png" ;this Section and ys stuff is to make the two buttons show on the same row on the Gui
;Gui, Add, Button, x238 y337 w100, Edit
Gui, Show, , L7 Player Simulation ;this is how you set the window title for the GUI and make the GUI visible
Gosub UpdateGui
Return

GuiClose: ;this automatically gets called when you hit the X (close) button on the Gui window 
ExitApp

ButtonPrev: ;Button clicked event handler subroutine
if (current > 1)
{
	current -= 1
	Gosub UpdateGui 
}
Return

ButtonNext: ;Button clicked event handler subroutine
if (current < filelist.MaxIndex())
{
	current += 1
	Gosub UpdateGui
}
Return

AirlineChosen:
Gui, Submit, NoHide
AirlineChoice := AirlineSelection
Gui, Destroy
Gosub StartPlayer
Return

MediaChosen:
Gui, Submit, NoHide
MediaChoice := MediaSelection
Gui, Destroy
Gosub StartPlayer
Return

UpdateGui:
FileRead synopsis, % textPath . filelist[current] ;unicode text will not display properly if you don't have FileEncoding UTF-8 set
synopsis := RegExReplace(synopsis, "<.*?>", "")
synopsis := RegExReplace(synopsis, "<br>", "`n")
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
