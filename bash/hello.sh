#!/bin/bash
#This is a comment
clear
Message="Hello World"
echo $Message
echo "Name of the shell or shell script: $0"
echo "First parameter: $1"
echo "Number of positional parameters: $#"
echo "Parameter list: $@"
echo "Exit status of the most recently executed foreground pipeline: $?"
echo "Process ID of the current shell: $$"
echo
echo "Use \\ to escape special characters to output the literal character, like \$"
echo 'Using single quoted strings, everything is literal: $Message $0 $1 $# $@ $? $$ \ \t \r\n \\ " etc, but you cant output single quotes or apostrophes'
echo "Double quoted strings do not preserve the literal values: \$ \` \\ - you can escape double quotes to output \"\" though"
echo
echo "Brace expansion:" {A,B,C}{1,2,3}{!,@,#}
echo "Tilde expansion - home:" ~
echo "Tilde expansion - pwd:" ~+
echo ${Message}
echo "Command expansion:" $(ls)
echo "Backtick expansion:" `ls`
echo "You can preserve newlines on command and backtick substitution by quoting:"
echo "`ls`"
echo "Arithmetic expansion $((3+5*8))"
echo "Arithmetic expansion $[3+5*8]"
echo "Filename expansion:" h*.sh he??o.??
