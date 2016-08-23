import eyed3
import codecs
import os
import re

f = codecs.open("results.txt", encoding='utf-8', mode='w')

root_path = r'C:\Users\Jason\Dropbox\My Stuff\Dev\Python\scripts\mp3_tagging\resources\1013 DigE Audio'

for root, dirs, files in os.walk(root_path):
    for filename in files:
        file_path = (os.path.join(root, filename))
        if filename.endswith(".mp3"):
            title = re.sub(r" - .*","",filename)
            artist = re.sub(r".* - ","",filename)
            artist = re.sub(r"\.mp3","",artist)
            for char in filename:
                if ord(char)>127:
                    f.write("Bad Filename:\t" + file_path + "\n")
                    #the main problem here is that I can't write non-ascii characters to a file for some reason
                    break
            audiofile = eyed3.load(file_path)
##            for char in audiofile.tag.artist:
##                if ord(char)>127:
##                    f.write("Bad XT Artist:\t" + char + "\t" + file_path + "\t" + audiofile.tag.artist)
##                    #Can't encode the character that is non-ASCII when writing to a file opened for read/write using default ASCII codec
##            for char in audiofile.tag.title:
##                if ord(char)>127:
##                    f.write("Bad XT Title:\t" + char + "\t" + file_path + "\t" + audiofile.tag.title)
##            print file_path + "\t" + title + "\t" + artist
            #f.write(file_path + "\t" + title + "\t" + artist + "\n")
f.close()
##    for filename in dirs:
##        #print(os.path.join(root, name))
##        print name

##directory_list = os.listdir(root_path)
##for filename in directory_list:
##    print filename
##    if filename.endswith(".mp3"):
##        title = re.sub(r" - .*","",filename)
##        artist = re.sub(r".* - ","",filename)
##        artist = re.sub(r"\.mp3","",artist)
##        #print title + "\t" + artist
##        audiofile = eyed3.load(file_path + "\\" + filename)
##        if audiofile.tag:
##            print audiofile.tag.artist
##            print audiofile.tag.title
