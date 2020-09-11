#! /usr/bin/env python

import random

n = 10
a = random.sample(xrange(n), n)

def selection_sort(a):
	for i in xrange(len(a)):
		m = i
		for j in xrange(i+1, len(a)): 
			if a[j] < a[m]: m = j
		a[i], a[m] = a[m], a[i]

selection_sort(a)	

