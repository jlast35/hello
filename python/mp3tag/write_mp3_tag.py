import re
import eyed3

# assumes an export text file exists that includes the correct path to the file to be tagged, and text for the artist and title fields to be tagged
f = open('export.txt')
for line in f:

    fields = line.split("\t")

    file_path = str(fields[0])
    artist = str(fields[1])
    title = str(fields[2].rstrip()) #get rid of the trailing \n

    # I have no idea why it is quoting certain strings on extraction, but cleanup
    file_path = re.sub('"',"",file_path)
    artist = re.sub('"',"",artist)
    title = re.sub('"',"",title)

    #print file_path + "\t" + artist + "\t" + title

    #tag the files
    audiofile = eyed3.load(file_path)
    print audiofile.tag.artist + " ---> " + audiofile.tag.title
    #audiofile.tag.artist = artist
    #audiofile.tag.title = title
    #audiofile.tag.save()
    
f.close()
