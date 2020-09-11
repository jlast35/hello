#! /usr/bin/env python

# Implementation of a Queue data structure
# Adds a few non-essential convenience functions

# Specifically, this is a node intended for a queue
class Node:
	def __init__(self, value):
		self.value = value
		self.nextNode = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def enq(self, value):
		# Create an empty node
		node = Node(value)
		# If it's the first node, make it the head
		if self.tail == None: self.head = node
		# Make its next node the current tail of the queue
		node.nextNode = self.tail
		# Update the tail to now be the new node
		self.tail = node

	def deq(self):
		# Special case: Empty
		if self.is_empty():
			#print "Deq empty!"
			pass
		# There is at least one node
		else:
			#print "Deq", self.head.value
			# Special case: only one node
			if self.is_singleton():
				# After we deq, head and tail are None
				self.tail = None
				self.head = None
			# There is more than one node
			else:
				penult = self.tail
				while penult.nextNode != self.head:
					penult = penult.nextNode
				#print "Penult is", penult.value
				penult.nextNode = None
				del self.head
				self.head = penult
		self.print_q()
			
	# ----- Convenience functions for testing -------

	def print_q(self):	
		if self.tail == None:
			#print "Empty queue!"
			pass
		else:
			current = self.tail
			while current != None:
				print current.value,
				current = current.nextNode
			print

	def from_list(self, qList):
		for node in qList: 
			self.enq(node)
			self.print_q()

	def is_empty(self):
		if (self.head == None) and (self.tail == None):	return True
		else: return False

	def is_singleton(self):
		if (self.head == self.tail) and (self.head != None): return True
		else: return False

	def deq_all(self):
		while not self.is_empty(): self.deq()

# ---------- TEST ----------------

q = Queue()

q.from_list(range(10))

q.deq_all()


