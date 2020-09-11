#! /usr/bin/env python

import random
import math

n = 1000000
a = random.sample(xrange(n), n)
#print a

# from the book - faster sequence
def shell_sort_2(a):
	n = len(a)
	#increment sequence divides roughly in thirds
	h=1
	while h<=n/(3*3): h=3*h+1
	while h>0:
		for i in xrange(h,n):
			v=a[i]
			j=i
			while j>=h and a[j-h]>v:
				a[j] = a[j-h]
				j-=h
			a[j]=v
		h/=3
	
# from website - less efficient but simpler
def shell_sort_1(a): 
	n = len(a)
	# increment sequence divides in half 
	h = n/2
	while h>0: 
		for i in xrange(h,n): 
			v=a[i] 
			# shift earlier gap-sorted elements up until the correct location for a[i] is found 
			j=i 
			while  j>=h and a[j-h]>v: 
				a[j] = a[j-h] 
				j-=h   
				# put temp (the original a[i]) in its correct location 
			a[j]=v 
		h/=2	


shell_sort_2(a)
#shell_sort_1(a)
#print a
