#! /usr/bin/env python

import random

# create a list of n random numbers
n = 10
a = random.sample(xrange(n), n)

def bubble_sort(a):
	for i in xrange(len(a),-1,-1):
		for j in xrange(1,i):
			if a[j-1] > a[j]:
				a[j], a[j-1] = a[j-1], a[j]

bubble_sort(a)	

