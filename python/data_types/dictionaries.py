d = {} #create an empty dictionary
d = dict() #cast an empty dictionary from nothing

d = {'a': 1, 'b': 1} #initialize a dictionary from literals

d2 = dict([('x',1), ('y',2)]) #cast a dictionary from a list if 2-tuples
print d2

d2 = dict(qa=1,r='arr',s=3) #this form only works if the keys given are strings
print d2

d3 = {(0,0,0): 0, (0,0,1): "hello"} #you can actually use any immutable type (such as a tuple) as a key value
print d3[(0,0,1)]

#you can use this function to create a dictionary from a key list such that all keys have the same value
print dict.fromkeys(['a','b'], "some value") 

keys = ['a','b','c','d']
values = [1,2,3,4]
print zip(keys,values) #zip creates a list of 2-tuples from 2 lists of equal length
#you can use such a list to create a dictionary via the dict() type cast
print dict(zip(keys,values))

#you can also use dictionary comprehension to create dictionaries -
print {key: value for (key, value) in zip(keys,values) if 1 < value < 4} #filter on values between 1 and 4 exclusive

#dictionaries (hash) map keys to objects - you can lookup the object associated with a key by indexing the key
print d['a'] #lookup a value by key
print d.get('c') #if you lookup a key this way, an invalid key returns None instead of throwing an exception on index
print d.get('c', 0) #you can also provide a default return value for invalid keys

#because the keys of a dictionary are part of a collection, you can test for membership
print d.has_key('a') #test a key value for membership in the dictionary
print 'a' in d #you can also test a key for membership like this

print d.keys() #list all keys - the list contains only unique values - it is set-like, similar to a function's domain
print d.values() #list all values associated with keys - the list of values may contain duplicates
#it is just a list of values associated with each key
#since it is not a set itself, it cannot be called the range, but is similar to the range except with duplicates
#in any case, because keys map 1:1 to a value, whenever the range is smaller than the domain, the values list will have duplicates

#dictionaries can grow - their size is not fixed
d2 = {'a': 3, 'd': 4}
d.update(d2) #the key,val pairs of d2 are added to d. d2 overwrites the key,val in d on collision
#dictionaries are mutable - they can be changed in-place by mutator methods such as update
print d

print d.pop('a') #returns the value associated with the key and removes the key from the dictionary
print d

del d['b'] #we can also just remove a key from a dictionary
print d

d['e'] = 5 #we can add an object to a dictionary by assignment - this creates or overwites the key and value

#dictionaries also have length - they have a countable number of key entries
print len(d)
#the length of a dictionary will always be the same as the length of its key list
#and the length of the key list will always be the same as the length of the value list because it is a 1:1 map
print len(d.keys()) == len(d.values()) == len(d)

#dictionaries are iterable - iterating over a dictionary actually iterates over its key list
for key in d:
    print key