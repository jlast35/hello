#module access
import re
from sys import stdin

#assignment
x = 1

#function definition
def square(x):
    return x*x

#function calls
x = square(2)

#print statement
print "Counting from 1 to 10 using a generator function:",

#generator definition
def countTo(x):
    for number in range(1,x+1):
        yield number

#for loop - using generator results
for number in countTo(10):
    if number == 2:
        continue
    elif number == 7:
        print " ...All right - stop already"
        break
    else:
        print number,
else: #this executes only if we get to the end of the loop without breaking first
    print "Finished counting!"

#pass is an empty place holder statement - no op / do nothing - intended to be replaced/overridden later
def doNothing():
    pass

#conditionals
if x == 1:
    print "x equals 1"
elif x == 2:
    print "x equals 2"
else:
    print "x does not equal 1 or 2"
    print "x equals", x 
