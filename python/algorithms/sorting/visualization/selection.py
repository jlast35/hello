#! /usr/bin/env python

import random, sys, time
from termcolor import colored

# create a list of n random numbers
n = 10
st = .7
a = random.sample(xrange(n), n)

def selection_sort(a):
	# we consider each value in the list from start to finish
	for i in xrange(len(a)):
		# minimum is assumed to be current location
		m = i
		# we search the rest of the list starting from current location
		# to find the minimum of what is left
		# we can ignore all previous processed values
		# because this algorithm guarantees they are already sorted
		for j in xrange(i+1, len(a)): 
			# we find the minimum value in the rest of the list
			if a[j] < a[m]: m = j
		# and swap the current location with the minimum

		print "\r",
		for l in a:
			if l == a[m]: print colored(l, "green"),
			elif l == a[i]: print colored(l, "red"),
			else: print l,
		sys.stdout.flush()
                time.sleep(st)

		a[i], a[m] = a[m], a[i]

		print "\r",
		for l in a:
			if l == a[i]: print colored(l, "green"),
			elif l == a[m]: print colored(l, "red"),
			else: print l,
		sys.stdout.flush()
                time.sleep(st)

selection_sort(a)	

