t = (1,2,3) #tuples can be defined explicitly with parenthesis and comma separated elements
t = 2, 3, 4 #tuples can be defined implicitly without parenthesis too
t = (1,) #to ensure that the one-tuple (1,) is not interpreted as (1) the value 1 in parenthesis, include the comma
t = () #you can also create an empty tuple
t = ('abc', [1,2,3], {1:2, 2:3, 3:4}) #tuples can contain any data type as elements

#tuples are immutable
#-you can't change them in-place with mutator methods like you can with lists or mutator objects
#although if an element of a tuple is itself mutable, you can still mutate the element within the tuple

#you can access each dimension/parameter/element of the tuple by index because they are sequential
print t[0] #indices into a tuple are zero-based
print t[1]
print t[2]

#because tuples are of fixed length, it makes sense to talk about the length of a tuple
print len(t) #when a tuple consists of nested objects, len(t) counts only the top level objects

#you can slice tuples (as with other sequences)
print t[0:2]

# + and * mean concatenate and repeat for sequences
print (1,2,3) + (4,5,6) #you can only concatenate a tuple to a tuple - also, both tuple literals must have parenthesis
#concatenating a tuple literal without parenthesis errors out: the + operator takes precedence over the commas
print (1,2,3) * 3 # the sequence repeat * operator must have an integer as one of its operands

#because tuples are sequences you can test for membership in them
print 1 in (1,2,3) #True
print (1,2) in (1,2,3) #False - the tuple (1,2) is not a top level element of (1,2,3) - don't confuse w/ set theory

#because tuples are sequences, you can iterate over them
for element in (1,2,3):
    print element

#you can cast an iterable object into a tuple
x = tuple([1,2,3])
x = tuple('strings are iterable sequences too')
print x

#you can count repeated elements in a tuple
print x.count('s')

#you can find the first occurrence of an element in a sequence and return its index
print x.index('g')
