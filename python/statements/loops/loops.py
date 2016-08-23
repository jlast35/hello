#When looping through a sequence,
#the position index and corresponding value can be retrieved at the same time
#using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

#To loop over two or more sequences at the same time,
#the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

#To loop over a sequence in reverse,
#first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(xrange(1,10,2)):
    print i

#To loop over a sequence in sorted order,
#use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f

#When looping through dictionaries,
#the key and corresponding value can be retrieved at the same time
#using the iteritems() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v

#To change a sequence you are iterating over while inside the loop
#(for example to duplicate certain items),
#it is recommended that you first make a copy.
#Looping over a sequence does not implicitly make a copy.
#The slice notation makes this especially convenient:
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print words