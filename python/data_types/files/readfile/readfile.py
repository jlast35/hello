file = open("utf-8_text_file.txt","r") #as you can see, we can open a UTF-8 file with or without BOM just as well as an ASCII file
for line in file:
    #when a line is read from a file, it also reads the newline characters at the end of the line
    print line.rstrip("\r\n") #print adds a \r\n to the line automatically after it prints
    #if you don't strip the newline characters before you print, then you get 2 newlines in a row
file.close()
