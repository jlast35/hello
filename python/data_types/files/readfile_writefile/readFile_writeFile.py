input_file = open("utf-8_text_file.txt","r")
output_file = open("output.txt","w")
for line in input_file:
    print line.rstrip("\r\n") #print adds a \r\n to the line automatically after it prints
    output_file.write(line) #we have to add the \r\n explicitly when writing to files
input_file.close()
output_file.close()