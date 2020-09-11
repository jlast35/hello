#! /usr/bin/env python

# Implementation of a Stack data structure
# Adds a couple of non-essential convenience functions

# Specifically, this is a node intended for a stack
class Node:
	def __init__(self, value):
		self.value = value
		self.nextNode = None

class Stack:
	def __init__(self):
		self.top = None


	def push(self, value):
		node = Node(value)
		node.nextNode = self.top
		#print "Push:", node.value  
		self.top = node
		self.print_stack()

	def pop(self):
		if self.top == None: 
			#print "Pop: Empty Stack!"
			return None
		else:
			node = self.top
			#print "Pop:", node.value
			self.top = node.nextNode
			self.print_stack()
			return node

	# ----- Convenience functions for testing -------

	def from_list(self, stackList):
		for node in stackList:
			self.push(node)
		return self

	def recursive_pop_all(self):
		while self.top != None:
			self.pop()
			self.recursive_pop_all()

	def print_stack(self):
		current = self.top
		while current != None:
			print current.value,
			current = current.nextNode
		print			

# ---------- TEST ----------------

stack = Stack().from_list(range(10))
stack.recursive_pop_all()

