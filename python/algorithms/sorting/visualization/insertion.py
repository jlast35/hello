#! /usr/bin/env python

# Note, even though this is called insertion sort,
# it's not like you're inserting a value into a list 
# and then sorting it to its spot
# it's more like: 
# consider each item from start to finish
# and until its previous is a lesser or equal value or start of list
# move it up the list 

import random, sys, time
from termcolor import colored

# create a list of n random numbers
#n = 10000
n = 10
st = 0.7
a = random.sample(xrange(n), n)

def insertion_sort(a):
	# go through each element from second to last
	# says 1, but remember: list index is zero based
	for i in xrange(1, len(a)):
		# we store the value at the current index
		# because we might overwrite it if shifting values forward
		# but we still need to remember it later when we find its spot
		v = a[i]
		print "\r",
		for l in a:
			if l == v: print colored(l, "red"),
			else: print l,
		sys.stdout.flush()
		time.sleep(st)
		# j starts from the same place as the current index
		j = i
		# we use j-1 to traverse backward through the list from i
		# at each step, if the list index j isn't zero yet
		# and the previous element is greater than the value at a[i]
		while (j>0) and (a[j-1] > v):
			# copy the value of the previous element to the current
			# in other words, move it up
			a[j] = a[j-1]
			# note that during processing, 
			# momentarily 2 adjacent spots have the same value
			# so the one in j-1 is unsettled until this loop ends
			# move the current index back one
			j -= 1
			# and repeat
			# this has the effect of 
			# shifting everything forward one spot
			# until we find out where the value goes
			# either at the front of the list
			# or the first spot where the previous value is <=
			# basically, float up as far as possible while smaller
		# once we arrive at either the beginning of the list j=0
		# or we find that the previous value is <= the value at i
		# that spot gets the value at i
		#print
		a[j] = v
		print "\r",
		for l in a:
			if l == v: print colored(l, "green"),
			else: print l,
		sys.stdout.flush()
		time.sleep(st)

insertion_sort(a)	
