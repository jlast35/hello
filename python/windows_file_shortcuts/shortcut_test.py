#import sys
import win32com.client 
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(r"M:\Integration Collateral\Music\2014\11\alaska.lnk")
print shortcut.TargetPath

#Note: this only works on Windows installations of Python
#it won't work on Cygwin or Linux because there is no win32com module in Linux installations of Python
