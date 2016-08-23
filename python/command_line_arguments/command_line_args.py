#!/usr/bin/env python

#the #! line is pretty much useless if this script does not specifically appear somewhere in the Cygwin path
#if you add "." to the PATH it should work...
#amazing.. Windows searches the current directory by default, but in Cygwin you have to tell it explicitly to do so

#really, if you want to be able to execute the file as a command,
#you either need to put each specific directory a command appears in in the PATH variable
#or else create a symlink to each executable command and put them all in a folder that IS in the path

#if you want to run the command without the extension, sorry - Cygwin doesn't support that
#you would have to write the filename itself without an extension an then use the #! line to tell it how to execute
#this works in Cygwin

#from a Windows command prompt, if the file extension is .py (extension must be present in the PATHEXT environment variable)
#and the file is in the current directory, then you can call the python script as a command without an extension
#Cygwin doesn't let you execute something "if it is in the current directory" - it must be in the PATH or it won't execute.

#what works in both is just to run the python script explicitly with: python script.py
#you can add any command line arguments you want after it
#any arguments given will be silently ignored by the script unless logic is written explicitly to process them
#distinct args must be separated by spaces - using more than one consecutive spaces is treated the same as one space

import sys
print sys.argv

for arg in sys.argv:
    print arg