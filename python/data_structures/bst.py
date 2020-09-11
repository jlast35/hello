#! /usr/bin/env python

import random
from collections import deque

class Node():
	def __init__(self, v):
		self.v = v 
		self.l = None
		self.r = None

class Binary_Search_Tree():

	def __init__(self): self.root = None

	# Insertion --------------------------------------
	
	# Insert so tree puts smaller nodes as left children
	# Binary trees are not allowed to have duplicate values
	def ins(self, n, st):
		if st == None: self.root = n
		else:
			if n.v < st.v:
				if st.l == None: st.l = n
				else: self.ins(n, st.l)
			elif n.v > st.v:
				if st.r == None: st.r = n
				else: self.ins(n, st.r)
			# Do not allow duplicate values
			# the following statement is not necessary
			# it just shows explicitly what happens by default
			elif n.v == st.v: return

	def ins_list(self, l):
		for v in l: self.ins(Node(v), self.root)


	# Recursive Traversals ------------------------------

	# Recursive pre-order traversal
	# Follows the same traversal path as depth-first search
	def pre_order(self, n):
		if n:
			print n.v,
			self.pre_order(n.l)
			self.pre_order(n.r)

	# For values in a sorted tree, in-order traversal actually outputs the values in sorted numerical order also
	def in_order(self, n):
		if n:
			self.in_order(n.l)
			print n.v,
			self.in_order(n.r)

	def post_order(self, n):
		if n:
			self.post_order(n.l)
			self.post_order(n.r)
			print n.v,

	# Searching ------------------------------------------

	# Iterative breadth first search
	def bfs(self):
		q = deque()
		q.append(self.root)
		while q:
			n = q.popleft()
			print n.v,
			# We queue the children left to right so the nodes on each level dequeue in left to right order
			if n.l: q.append(n.l)
			if n.r: q.append(n.r)
		print

	# Iterative depth first search
	# Follows same traversal path as pre-order, without using the function call stack
	def dfs(self):
		# In recursive pre-order traversal, the function call stack is implicitly used to push and pop nodes
		# In dfs, we still use a stack, except we create it ourselves and iterate though it explicitly
		# The Python library deque is interchangeably usable for stacks, queues, and deques		
		if not self.root:
			print "Empty tree"
		else:
			stack = deque()
			stack.append(self.root)
			#print self.root.v
			while stack:
				n = stack.pop()
				print n.v,
				# We push nodes to the stack in reverse order so left pops first
				if n.r: stack.append(n.r)
				if n.l: stack.append(n.l)
			print


	# Deletion --------------------------------------------------------------------------------------------

	# the main problem is that you have to know about the p node in order to delete a node from a tree.
	# so we will keep track of it via parameter.  that way we can even call this recursively on subtrees

	# Recursive delete - with helper functions -----------------------------
	def delete(self, n, v, p):
		if not n: return 
		if v == n.v: self.promote(n, p)
		if v < n.v: self.delete(n.l, v, n)
		if v > n.v: self.delete(n.r, v, n)

	def promote(self, n, p):
		if n.l and n.r:	self.promote_leftmost_successor_of_right_subtree(n)
		else: self.promote_immediate_successor(n, p)

	def find_immediate_successor(self, n):
		if n.l: return n.l
		if n.r: return n.r

	def promote_immediate_successor(self, n, p):
		s = self.find_immediate_successor(n)
		if not p: self.root = s
		elif p.l and (p.l.v == n.v): p.l = s
		else: p.r = s
		del n

	def find_leftmost_successor(self, n):
		if not n.l: return n
		else: return self.find_leftmost_successor(n.l)

	def promote_leftmost_successor_of_right_subtree(self, n):
		s = self.find_leftmost_successor(n.r)
		n.v, s.v = s.v, n.v
		self.delete(n.r, s.v, n)

	# an iterative solution does not have call stack limitations, uses less memory, and runs slightly faster

	# Iterative delete ----------------------------------------------------------
	def delete_iterative(self, n, v, p):
		while n:
			if v == n.v:
				if n.l and n.r:	
					s = n.r
					while s.l: s = s.l
					n.v, s.v = s.v, n.v
					p = n
					n = n.r
					v = s.v
				else: 
					s = None
					if n.l: s = n.l
					elif n.r: s = n.r
					if not p: self.root = s
					elif p.l and (p.l.v == v): p.l = s
					else: p.r = s
					del n
					return
			elif v < n.v:
				p = n
				n = n.l
			elif v > n.v:
				p = n
				n = n.r


# Test -------------------------------------------------------------------------------------------------------

t = Binary_Search_Tree()
l = random.sample(xrange(100), 30)
t.ins_list(l)
t.pre_order(t.root)
print
t.in_order(t.root)
print
t.post_order(t.root)
print
t.bfs()
t.dfs()
print

#random.shuffle(l)

# Delete all nodes in same order as they were inserted using iterative delete
for v in l:
	t.delete_iterative(t.root, v, None)
	t.dfs()

t.ins_list(l)


# Delete all nodes in same order as they were inserted using recursive delete
for v in l:
	t.delete(t.root, v, None)
	t.dfs()

# Repeatedly delete root node until tree is empty
#while (t.root):
#	#t.delete(t.root, t.root.v, None)
#	t.delete(t.root, t.find_min(t.root).v, None)
#	t.dfs()
print l
