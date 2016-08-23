def print_text(string_parameter): #function declaration with 1 parameter - DON'T forget the colon!
    print string_parameter #body of function - must be indented

text_to_print = "Printing string variable passed to function parameter" #store some text in a variable

print_text(text_to_print) #can we pass a variable to a function parameter? yes

print_text("Printing string literal text passed to function parameter") #can we pass a literal value to a parameter? yes

#print_text()
#what happens when we fail to pass a required parameter? -uncomment the above line if you want to see for yourself
#parameter not supplied results in - TypeError: print_text() takes exactly 1 argument (0 given)