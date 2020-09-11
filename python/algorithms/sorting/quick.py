#! /usr/bin/env python

import random

n = 100000000
a = random.sample(xrange(n), n)
#print a

def partition(a, l, r):
	i=l-1
	v=a[r]
	for j in range(l, r):
		if a[j] <= v:
			i+=1
			# swap(a,i,j)
			a[i], a[j] = a[j], a[i]
	# swap(a,i+1,r)
	a[i+1], a[r] = a[r], a[i+1]
	return i+1

def quick_sort(a, l=0, r=len(a)-1):
	if r > l:
		i = partition(a, l, r)
		quick_sort(a, l, i-1)
		quick_sort(a, i+1, r)
  
#quick_sort(a)
a.sort()
#print a
