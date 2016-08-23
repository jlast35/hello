list = ["a","d","c"]

integer_list = range(10) #you can use the range function to generate a list of integers

#you can also generate lists using list comprehension syntax - covered separately

print list

#you can do all the usual sequence operations on lists:
# slice [:], index [], count() elements, concatenate (+), repeat (*),
#find the index() of the first occurrence of an element
#you can also find the min() or max() value of an iterable collection 

print list.index("c")
print list.count("a")
print list[0]
print list[1:]
print max(list)
print min(list)
print list + ["x","y","z"]
print list * 4

list + ["e"] #concatenation does not persist (does not mutate the list in place) - it creates a new list
list += ["e"] #concatenation with assignment persists - 
print list

#lists are collections, so you can test for membership
print "d" in list

#lists have length, so you can take the len() of a list
print len(list) # len tells us how many items are in the list (one based)

print range(len(list))#range returns a list of numbers from 0 to its argument minus 1 - useful for indexing arrays

for index in range(len(list)): 
    print list[index],
print

#lists are iterable, so you can iterate over them - for element in [1,2,3]
for element in list: #there is more than one way to iterate over the elements in a list
    print element,
print

#lists are not fixed length
#you can append, extend, insert, del, remove, pop
list.append("b") #appending to a list persists - it does not create a new list
print list

list.extend(["x","y","z"])
print list

list.pop()
print list

list.remove("x")
print list

list.insert(2,"!")
print list

del list[0:2] #you can use del with indices or slices
print list

#lists are mutable - you can change them in place
#you can sort them, reverse them
list.sort()
print list #lists are mutable - you don't have to assign the results of the sort to the list variable - they remain

list.reverse()
print list
#print list.reverse() prints None because that's what the function returns when successful - it doesn't return the list itself
#it's an in-place mutation procedure - it doesn't return anything
