#! /usr/bin/env python

import random

n = 10000000
a = random.sample(xrange(n), n)

# Python program for implementation of Radix Sort 

# A function to do counting sort of a[] according to 
# the digit represented by exp. 
def counting_sort(a, e, b=10): 
	n = len(a) 

	# The output array elements that will have sorted a 
	o = [0]*(n) 

	# initialize count array as 0 
	c = [0]*(b) 

	# Store count of occurrences in count[] 
	for i in xrange(0, n): 
		x=(a[i]/e) 
		c[(x)%b]+=1

	# Change count[i] so that count[i] now contains actual 
	# position of this digit in output array o 
	for i in range(1,b): c[i] += c[i-1] 

	# Build the o array 
	i = n-1
	while i>=0: 
		x = (a[i]/e) 
		o[c[(x)%b]-1]=a[i] 
		c[(x)%b]-=1
		i-=1

	# Copying the o array to a[], 
	# so that a now contains sorted numbers 
	for i in xrange(0,len(a)): a[i]=o[i] 

# Method to do Radix Sort 
def radix_sort(a, b=10): 
	# Find the maximum number to know number of digits 
	m = max(a) 

	# Do counting sort for every digit. Note that instead 
	# of passing digit number, exp is passed. exp is b^i 
	# where i is current digit number 
	e=1
	while m/e>0: 
		counting_sort(a,e) 
		e*=b

# Driver code to test above 
radix_sort(a,b=10) 
#print a

# This code is contributed by Mohit Kumra 

