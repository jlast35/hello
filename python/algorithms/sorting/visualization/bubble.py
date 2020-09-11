#! /usr/bin/env python

import random, sys, time
from termcolor import colored

# create a list of n random numbers
n = 10
a = random.sample(xrange(n), n)
st = .7

def bubble_sort(a):
	for i in xrange(len(a),-1,-1):
		for j in xrange(1,i):
			if a[j-1] > a[j]:

				print "\r",
				for l in a:
					if l == a[j]: print colored(l, "green"),
					elif l == a[j-1]: print colored(l, "red"),
					else: print l,
				sys.stdout.flush()
				time.sleep(st)

				a[j], a[j-1] = a[j-1], a[j]

				print "\r",
				for l in a:
					if l == a[j]: print colored(l, "red"),
					elif l == a[j-1]: print colored(l, "green"),
					else: print l,
				sys.stdout.flush()
				time.sleep(st)
			else:
				print "\r",
                                for l in a:
                                        if l == a[j]: print colored(l, "yellow"),
                                        elif l == a[j-1]: print colored(l, "yellow"),
                                        else: print l,
                                sys.stdout.flush()
                                time.sleep(st)

bubble_sort(a)	

