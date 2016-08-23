#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
;the stuff above is all boiler-plate code you get on creating a new AHK script 

;array := ["A", "B", "C"] ;you can initialize an array this way
;array := array("A", "B", "C") ;you can also initialize an array this way
array := [] ;you can even initialize an empty array
array.Insert("A") ;but in order to insert to an array, you must at least have first assigned the variable to an empty array
array.Insert(B) ;if you don't enclose the B in quotes, it thinks you mean the variable B, not the string "B"
min := array.MinIndex() ;if you use = instead of := it assigns the literal text "array.MinIndex()" to min rather than what it evaluates to.
max := array.MaxIndex() ;again, you have to use := whenever you want to assign the result of an expression to a variable rather than the literal text
MsgBox % min . " -> " . max ;we use %space to force evaluation of an expression for use as a parameter - the space.space means concatenate
For index, value in array
	MsgBox % index ":" value ;you can also omit the . and concatenate with just space
MsgBox % array[100] ;if you index an array out of bounds, it returns nothing (an empty string actually)
Return
;if you don't define a hotkey, the script will just execute as a normal program until it sees a return statement and exits
;note that if you comment on the same line as a statement, you must have a space before the initial ; of the comment