import re
input_file = open("log.txt","r")

for line in input_file:
	if re.search(r"\t",line):
		print "Tab Found:" + line.replace("\t"," - ")
input_file.close()
