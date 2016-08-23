#let's test some string encoding - ASCII and unicode
import unicodedata

print 'ASCII string literal'

print u'Unicode conversion of ASCII string literal' #convert a string literal to unicode

s = 'Unicode conversion of ASCII string variable'
print unicode(s)

print chr(255) #prints FF - it's not an ASCII char 0-127 so it prints the hex in a black box - the type is string
print '\xFF' #same as above - note: the escape sequence for a hex character \x## reads exactly 2 nibbles of hex 00-FF
print '\xFFF - notice that the 3rd F is not part of the character escape sequence \\xFFF'
#print '\xF'
#print '\xFG'
##ValueError: invalid \x escape

#print chr(256) #ValueError: chr() arg not in range(256)

#the unicode conversion function works as follows:
##unicode(string[, encoding, errors])
#if you leave off the encoding argument, ASCII encoding is used as the default, so chars >= 128 are errors
#errors='replace' replaces the text it can't convert \u#### hex
#errors='ignore' simply omits the text it can't convert from the output

unicode(chr(127)) #this unicode conversion works fine
#unicode(chr(255)) #this one does not
##UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 0: ordinal not in range(128)
#unicode(chr(256)) #this one does not either - it throws the following chr error first in case you were wondering
##ValueError: chr() arg not in range(256)

u = u"Hello World..."+unichr(233) #you can append a unicode character unichr(0..) to a unicode string, but not an ASCII character chr(0..127)
for i, c in enumerate(u):
    print i, '%04x' % ord(c), unicodedata.category(c),
    print unicodedata.name(c)