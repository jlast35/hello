s1 = set() #create an empty set
s1 = {'apples', 'oranges', 'bananas'} #create a set from literals
print s1

#you can also create sets via set comprehension syntax:
print {x for x in ["good","bad","ugly"] if x != "ugly"}

s2 = set(['oranges','peaches','pineapples','grapes']) #cast a set from a list

s3 = {'apples','oranges'}

vehicle_list = ['planes','trains','automobiles']
s4 = set(vehicle_list) #cast a set from a list
print s4

s5 = s1.copy() #create a shallow copy of s1

print 'strawberries' in s2 #test set membership
s2.add('strawberries') #add an element to a set
print 'strawberries' in s2
print 'xyzzy' not in s2
s2.remove('strawberries') #remove an element from a set - must be a member or it throws an exception
s2.discard('xyzzy') #removes it if it is a member - does not throw an exception if it's not
print s2.pop() #removes an arbitrary element from a set and returns it - set must be non-empty or throws exception
print s2 #the element popped is arbitrary - not random - it's the same each run

#union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset()
#you could use these named functions, but why? - operators look better
#-it seems to be that they are useful because the argument to the named functions can be any iterable - not just sets
#but operators require sets, otherwise the operator overloading does not hold and may throw errors

print s3 < s1 #proper subset - sets can't be equal
print s1 < s3
print s1 < s1
print s3 <= s1 #subset - sets can be equal
print s1 <= s3
print s3 <= s3

print s1 > s3 #proper superset - sets can't be equal
print s3 > s1
print s3 > s3
print s1 >= s3 #superset - sets can be equal
print s3 >= s1
print s1 >= s1

print s1 | s2 #union - you might be tempted to use s1+s2 for union instead, but that throws an exception. + is for sequences  
print s1 & s2 #intersection
print s1 - s2 #difference - elements in s1 that are not in s2
print s1 ^ s2 #symmetric difference - elements in either set but not both
# you can tack assignment onto any of those operators: s1 |= s2,  s1 &= s2,  s1 -= s2,  s1 ^= s2 are all valid
# you can also chain operators like: s123 = s1|s2|s3

print s1.isdisjoint(s4) # true iff (s1 intersect s4) == {}
#if 2 non-empty sets are disjoint, then a < b, a > b, and a == b can all be false at once
#thus, sets are not orderable

s1.clear() #remove all elements from the set
print s1

print s5 #s5 was a copy of s1 - note that clearing s1 did not also clear s5

s1 = {'a','b'}
s2 = {'b','a'}
print s1 == s2 #in sets, order does not matter - 2 sets are equal if they both contain the same elements
#(s1 == s2) iff (s1 <= s2) and (s2 <= s1)
