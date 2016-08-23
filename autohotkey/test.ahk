; AZAL Music Input Auto-HotKey script
; Programmed by: Jason Anderson 3/27/2014
; ===================================
; Assumes you have copied to clipboard an album worth of excel data, however many rows are in a given album
; where each row is a tab delimited 4-tuple consisting of {artist, title, track number, duration in seconds}
; and each row is separated from the next with a carriage return
; Also assumes you have logged into the AZAL website and are on the Track / Sequence tab of the album, on the English tab
; It also assumes that all previous tracks have already been deleted from the album and that you have clicked to place your cursor in the blank Track/Artist text field
; The web page must be maximized and in-focus on the right-most monitor screen (my Dell monitor) with the page's rightmost scroll bar all the way up
; Also assumes that AZAL has not changed the layout of their webpage since 3/27/2014 when this was written.
; Also, once you start the script, you should not move the mouse or type any key until the script is finished or it may throw off the rest of the input.
; ***If any of these conditions fail to hold true, this script will likely not work!
; ====================================

; Press {Ctrl+Shift Z} to start this script
$^+z::
KeyWait Control
KeyWait Shift

SendMode Input
; store the contents of the clipboard to a variable
text = %clipboard%
text := RegExReplace(text, "\r\n$")

; run a parse loop on the contents of the clipboard
; NOTE: if you try to parse the carriage return row delimiters in any other way than {(delimiters), (excludes)} as `n, `r , things get messed up like sending {Enter} sends twice, the loop parses incorrectly, etc 
Loop, parse, text, `r, `n
{
	; click "create new entry" before all but the first row
	ifNotEqual A_Index, 1
	{
		;Click 1135,430
		;Sleep 6000
	}
	
	; make sure we are starting our text input from the beginning of the track/artist text box
	;Click 834,463

	; for each line (each row of the spreadsheet on the clipboard actually), parse out each tab separated field in order
	line = %A_LoopField%
	Loop, parse, line, %A_Tab%
	{
		ifNotEqual A_Index, 1
		{
			Send %A_Tab%
		}
		; as we parse out each field, send the text to the current text box, then tab over to the next one
		Send %A_LoopField%
	}
	Send {Enter}
	
	; after you're done with inputting each field, click the "save changes" button
	;Click 719,565
	;Sleep 6000

;and then go back to the top of the loop to see if there are more rows to process
}

;click arabic
;Click 700,381
;Sleep 6000
;click copy all tracks
;Click 1043,403
;Sleep 6000

;click azerbaijani
;Click 810,381
;Sleep 6000
;click copy all tracks
;Click 1043,403

; Done processing this album - for now, you'll have to manually delete the extra empty track that seems to be getting created at the tail of the loop for some reason
; Then select the next album, copy its data from excel to the clipboard, and re-run this auto-hotkey script. 