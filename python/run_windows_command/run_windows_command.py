#!/usr/bin/env python

#this script requires PDNBulkUpdaterCmd and Paint.NET 3.5.11 to be properly installed on this machine for it to work
from subprocess import call
import os


path_to_paintNET = "C:\Program Files\Paint.NET"

os.chdir(path_to_paintNET) #if you don't do this, then PDNBulkUpdaterCmd won't work, because it expects to be called from here and looks for the Effects sub-folder relative to the path the command was actually executed from 

#please use quoted strings ie: '"C:\this path has spaces.txt"' for pathnames because the windows command line won't work right otherwise
path_to_PDNBulkUpdaterCmd = '"C:\Program Files\Paint.NET\PDNBulkUpdaterCmd.exe"'
path_to_image_file_to_process = '"C:\Users\Jason\Dropbox\My Stuff\Dev\Python\scripts\download_file\matrix.jpg"'
path_to_output_directory = '"C:\Users\Jason\Dropbox\My Stuff\Dev\Python\scripts\download_file"'
target_resolution = '165x218'
target_file_type = 'png'
target_filename_without_extension = '"TheMatrix"'

windows_command = path_to_PDNBulkUpdaterCmd + ' ' + path_to_image_file_to_process + ' /o:' + path_to_output_directory + ' /res:' + target_resolution + ' /oft:' + target_file_type + ' /ren:' + target_filename_without_extension

#cygwin_command = "convert matrix.jpg -resize '165x218!' -quality 100 matrix.png"
#call(cygwin_command, shell=True)
call(windows_command, shell=True)
