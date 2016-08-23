import re
input_file = open("CaptainPhillips-TheatricalAirline_jpn-r1.txt","r")
output_file = open("output_file.txt","w")

text = ""
for line in input_file:
    text = text + line

text = re.sub(r"^Lambda.*\n\n",r"",text) #get rid of the 2 header lines - they aren't used in fixed srt subtitle format
#reformat the data for the first (numbered) subtitle data line in each block - the subtitle line number is always 1, the time code uses ##:##:##,##0 --> ##:##:##,##0 format, the actual text starts on the next line
text = re.sub(r"^([^\t])+\t(\d\d)(\d\d)(\d\d)(\d\d)/(\d\d)(\d\d)(\d\d)(\d\d)\t(.*\n)",r"1\n\2:\3:\4,\g<5>0 --> \6:\7:\8,\g<9>0\n\g<10>",text, flags=re.MULTILINE)

#first of all, sub does not replace ALL matches in a block of multi-line text unless executed with the re.MULTILINE flag
#second, whereas in notepad++, unmatched optional groups return an empty string, in python they throw an "unmatched group" error when referenced...
#invalid backreferences return an error in Python, whereas in Perl they return an empty string.
#This is precisely why the same regex that worked in Notepad++ doesn't work for Python.
#So, you have to decompose the regex into several lines so that you don't run into a failed backreference with no way to get it to return empty.
text = re.sub(r"^\t{4}",r"",text, flags=re.MULTILINE) #remove the leading 4 tabs from each subtitle line that appears simultaneously with the first
text = re.sub(r"^(1\n.+?)(?=1\n)",r"\1\n",text,flags=re.MULTILINE|re.DOTALL)
#make sure the above match blob is lazy .+? instead of greedy or it will try to grab all the text down to the final 1\n start delimiter in the file - dotall matches newline characters and keeps going
#make sure you don't consume the 1/n section delimiter at the end (?=...) because it is also the start delimiter for the next block
print text
output_file.write(text)

#matches = re.finditer(r"^([^\t])+\t(\d\d)(\d\d)(\d\d)(\d\d)/(\d\d)(\d\d)(\d\d)(\d\d)\t(.*\n)(\t{4}(.*\n))?(\t{4}(.*\n))?(\t{4}(.*\n))?", text,flags=re.MULTILINE)
#for match in matches:
#    print match.group()

input_file.close()
output_file.close()