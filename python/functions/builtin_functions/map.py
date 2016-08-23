def compare(a,b):
    print str(a) + " =? " + str(b) + " : " + str(a == b)
    return a == b

x = [1,2,3]
y = [1,2,4]

results = map(compare, x, y)
print results

#so.. map takes a function and some arbitrary number of input lists...
#it applies the function to each set of parameters in turn
#and returns the collective results as a list

import operator
print reduce(operator.and_, results)
print reduce((lambda x, y : x or y), results)

strings = ['A','','B','','','C']
print filter(operator.truth, strings)

