#numeric types - int, long, float, complex
#real types - int, long, float
#integer types - int, long

#there are also rational and integral number types apparently...

#you may not use most of these ever except int and float for basic math
#just be aware that other types do exist, and research the documentation as needed.

#regular integers
x = 1234 

#long integers end with an L or l - don't use the letter l - it looks too much like the number 1
x = 9999999999999999999999999999999999999L 
x = 9999999999999999999999999999999999999l
x = 9999999999999999999999999999999999999  #python automatically stores integers as longs if > 32 bits

#floats
x = 1.23
x = 3.14e-10 #exponent notation is e or E, - or + (+ is default if omitted), exponent
x = 4E210
x = 4.0e+210
print (1.0).is_integer() #True
print (1.3).is_integer() #False

#special values for floats
x = float('nan') #special float: not a number
x = float('inf') #special float: infinity
x = float('+inf') #special float: positive infinity - same as inf
x = float('-inf') #special float: negative infinity

x = 0177 #octal
x = 0x9ff #hex - lower case
x = 0XFF #hex - upper case
x = 0b100 #binary

#hex numbers can't have decimal point values - for hex it returns an error
#octal numbers can't have decimal point values
#for octal, the moment you add a decimal, the number is interpreted as a zero-padded base 10 float instead

#base conversion - these all return strings
x = hex(123)
x = bin(123)
x = oct(123)

#you can also convert whole number 'strings' of an arbitrary base (between 2 and 36) to base 10 integers
#as long as the string does not contain any non-base-appropriate characters
x = int('123', base=5)
x = int('123xyz',base=36)

#complex (aka imaginary) numbers
x = 3+4j
x = 3.0+4.0j #works with floats
x = 3J #works with no real part
x = complex(1,2) # = 1+2j an alternate way of constructing/using complex numbers

x = (1+2j).imag #use just the imaginary component
x = (1+2j).real #use just the real component

#type casting
x = int(1.23)
x = float(24)
x = long(4.7) #long truncates decimals
x = complex(5.2)
#of course, you can cast any of these to string types using str(number), but then they are no longer numbers

#automatic up-conversion of types
print type(1)
print type(1 + 2.3) #int -> float
print type(1+2L) #int -> long
print type(1.2+3L) #long -> float
print type(0xf) #hex is not a type; it's a format - int is the type
print type(3e10) #exponent notation is not a type; it's a format of float
print type(3J) #imaginary component without a real component
print type(3L+4j) #long -> complex

#boolean values are just the numbers 0 and 1
x = bool(3) # = True
x = bool(0) # = False
print True + 1 # = 2
print False * 5 # = 0