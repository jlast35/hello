file = open("myfile.txt","w")
file.close()
#if the file does not exist and you open it in write mode "w", it creates the file
#if the file does not exist and you open it in read mode "r" or no 2nd argument, it throws a File not found error.
