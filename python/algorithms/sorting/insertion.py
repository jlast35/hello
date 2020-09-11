#! /usr/bin/env python

import random

n = 10000
a = random.sample(xrange(n), n)

def insertion_sort(a):
	for i in xrange(1, len(a)):
		v = a[i]
		j = i
		while (j>0) and (a[j-1] > v):
			a[j] = a[j-1]
			j -= 1
		a[j] = v

insertion_sort(a)	
