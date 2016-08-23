#!/usr/bin/python

#import codecs, sys

# !!! making utf8 the default encoding may cause problems with other standard python modules
#reload(sys)
#sys.setdefaultencoding('utf-8')

# !!! setting the code page causes io issues
#import win32console
#win32console.SetConsoleCP(65001)
#win32console.SetConsoleOutputCP(65001)

#print sys.getdefaultencoding()

##if sys.platform == 'win32':
##    try:
##        import win32console 
##    except:
##        print "Python Win32 Extensions module is required.\n You can download it from https://sourceforge.net/projects/pywin32/ (x86 and x64 builds are available)\n"
##        exit(-1)
##    # win32console implementation  of SetConsoleCP does not return a value
##    # CP_UTF8 = 65001
##    win32console.SetConsoleCP(65001)
##    if (win32console.GetConsoleCP() != 65001):
##        raise Exception ("Cannot set console codepage to 65001 (UTF-8)")
##        print "1"
##    win32console.SetConsoleOutputCP(65001)
##    if (win32console.GetConsoleOutputCP() != 65001):
##        raise Exception ("Cannot set console output codepage to 65001 (UTF-8)")
##        print "2"

#use this to apply to all print statements in the current script
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

text = codecs.open("unicode.txt", encoding="utf-8")
#text = open("unicode.txt")
for line in text:
    print line #.encode("utf-8")  #you can do this on a per line basis - BUT ONLY IF you have NOT ALSO used:  sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
