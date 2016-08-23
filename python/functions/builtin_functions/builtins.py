numberList = [3,1,2]

print min(numberList)
print max(numberList)
print sum(numberList)

print len(numberList)

print filter((lambda x: x > 1), numberList)
print reduce((lambda x,y: x * y), numberList)
print map((lambda x: x + 5), numberList)

print sorted(numberList)
print numberList
print sorted(numberList,reverse=True)

print cmp(1,1)
print cmp(1,3)
print cmp(3,1)
print cmp("a","b")

print range(1,11,2)

booleanList = [True,True,False]

print any(booleanList)
print not any(booleanList)

print all(booleanList)
print not all(booleanList)

print bool("")

print list(enumerate(['a','b','c'],1))

exec('print "Hello"')

print set(['a','b','b','c'])

print zip([1,2,3],['a','b','c'])
#------------------- Number conversion
print oct(10)
print bin(10)
print hex(10)
print int("10")
print int("1011210212121",base=3)
print long("10")
#------------------ Math
print abs(-4)
print divmod(11,7)
#------------------ Character conversion
print ord("a")
print chr(97)
print unichr(1234)
#----------------- ASCII and Unicode strings
print str(1234)
print unicode("Unicode String")
