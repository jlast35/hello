#! /usr/bin/env python

import random, sys
from collections import deque

class Node():
	def __init__(self, v):
		self.v = v 
		self.l = None
		self.r = None
		self.c = None 
		self.p = None

class Red_Black_Tree():

	def __init__(self): 
		self.root = None

	# Insertion --------------------------------------
	
	# Insert so tree puts smaller nodes as left children
	# Binary trees are not allowed to have duplicate values
	def rb_ins(self, n):
		print
		self.dfs()
		print "Inserting", n.v
		# 1 perform standard bst insert
		self.bst_ins(n, self.root)
		# make the color of the newly inserted node red
		n.c = "Red"

		self.rebalance(n)

	def rebalance(self, n):
		print "rebalancing"
		# 2 if n is root, change color of new node to black
		if self.root == n: 
			print n.v, "is root. Making it black."
			n.c = "Black"

		# 3 if n is not root AND the parent of n is not black
		# again... the "parent" problem.  how do you keep track of parents and grandparents?
		elif (not n == self.root) and (n.p.c == "Red"):
			uc = self.get_uncle_color(n)
			# a) if Red uncle:
			if uc == "Red":
				print n.v, "has a Red uncle"
				self.process_red_uncle(n)
			# b) if Black uncle:
			elif uc == "Black": 
				print n.v, "has a Black uncle"
				self.process_black_uncle(n)
		else:
			print n.v, "has a Black parent. Leaving it alone."

	def process_red_uncle(self, n):
		u = self.get_uncle(n)
		# change color of parent and uncle to black
		n.p.c = "Black"
		u.c = "Black"
		print "Changing parent", n.p.v, "and uncle", u.v, "to black"
		# change grandparent red
		if n.p and n.p.p: 
			print n.p.p.v, "Changing grandparent red"
			n.p.p.c = "Red"
			self.rebalance(n.p.p)
	
	def check_values(self, n, p, g):
		if n.l: print "nlp", n.v, n.l.p.v 
		if n.r: print "nrp", n.v, n.r.p.v 
		if p.l: print "plp", p.v, p.l.p.v 
		if p.r: print "prp", p.v, p.r.p.v 
		if g.l: print "glp", g.v, g.l.p.v 
		if g.r: print "grp", g.v, g.r.p.v 

	
	def do_case_ll(self, n):
		print "LL"
		print "Right rotate g"
		# shortcuts
		p = n.p
		g = p.p
		
		print "n", n.v, "p", p.v, "g", g.v
		# g should become the new right child of p
		# p's right child should become the new left child of g
		print "Before"
		self.check_values(n, p, g)

		s = p.r
		p.r = g		
		g.l = s

		# update the parents of the changed nodes
		t = g.p
		p.p = t
		g.p = p
		if not t: self.root = p
		elif t.l and (t.l == g): t.l = p 
		elif t.r and (t.r == g): t.r = p
		if g.l: g.l.p = g

		print "After"
		self.check_values(n, p, g)

		print "Swap colors of g and p"
		# swap colors of g and p
		p.c, g.c = g.c, p.c

	def do_case_lr(self, n):
		print "LR"
		print "Left rotate p"
		# shortcuts
		p = n.p
		g = p.p

		print "n", n.v, "p", p.v, "g", g.v
		print "Before"
		self.check_values(n, p, g)

		t = n.l
		n.l = p
		p.r = t

		# update parents
		g.l = n
		n.p = g
		p.p = n
		if p.r: p.r.p = p

		print "After"
		self.check_values(n, p, g)
		
		self.dfs()

		print "Do LL"
		self.do_case_ll(p)

	def do_case_rl(self, n):
		print "RL"
		print "Right rotate p"
		# shortcuts
		p = n.p
		g = p.p

		print "n", n.v, "p", p.v, "g", g.v
		print "Before"
		self.check_values(n, p, g)

		t = n.r
		n.r = p
		p.l = t

		# update parents
		g.r = n
		n.p = g
		p.p = n
		if p.l: p.l.p = p

		print "After"
		self.check_values(n, p, g)

		self.dfs()

		print "Do RR"
		self.do_case_rr(p)

	def do_case_rr(self, n):
		print "RR"
		print "Left rotate g"
		# shortcuts
		p = n.p
		g = p.p
		
		print "n", n.v, "p", p.v, "g", g.v
		# g should become the new right child of p
		# p's right child should become the new left child of g
		print "Before"
		self.check_values(n, p, g)

		s = p.l
		p.l = g		
		g.r = s

		# update the parents of the changed nodes
		t = g.p
		p.p = t
		g.p = p
		if not t: self.root = p
		elif t.l and (t.l == g): t.l = p 
		elif t.r and (t.r == g): t.r = p
		if g.r: g.r.p = g

		print "After"
		self.check_values(n, p, g)

		print "Swap colors of g and p"
		# swap colors of g and p
		p.c, g.c = g.c, p.c

	def process_black_uncle(self, n):
		p = n.p
		g = p.p
		if g.l and (g.l.v == p.v):
			if p.l and (p.l.v == n.v): self.do_case_ll(n)
			elif p.r and (p.r.v == n.v): self.do_case_lr(n)
		elif g.r and (g.r.v == p.v):
			if p.r and (p.r.v == n.v): self.do_case_rr(n)
			elif p.l and (p.l.v == n.v): self.do_case_rl(n)
		else:
			print "Subcase not found"

	def get_color(self, n):		
		if not n: return "Black"
		else: return n.c

	def get_uncle_color(self, n):
		u = self.get_uncle(n)
		return self.get_color(u)
	
	def get_uncle(self, n):
		if n.p and n.p.p: g = n.p.p
		else: return None
		if g.l and (g.l.v == n.p.v):
			if g.r:	return g.r
			else: return None 
		elif g.r and (g.r.v == n.p.v): 
			if g.l: return g.l
			else: return None

	def bst_ins(self, n, st):
		if st == None: 
			self.root = n
		else:
			n.p = st
			if n.v < st.v:
				if st.l == None: st.l = n
				else: self.bst_ins(n, st.l)
			elif n.v > st.v:
				if st.r == None: st.r = n
				else: self.bst_ins(n, st.r)


	def rb_ins_list(self, l):
		for v in l: 
			self.rb_ins(Node(v))

			# Paranoid validity check after every insert

			#if not self.is_valid_red_black_tree():
			#	print "Something went wrong on insert", v
			#	self.dfs()
			#	sys.exit()
		print

	# Iterative depth first search
	def dfs(self):
		if not self.root:
			print "Empty tree"
		else:
			stack = deque()
			stack.append(self.root)
			while stack:
				n = stack.pop()
				print n.v, ":", n.c,
				if n.p: print "p", n.p.v,
				else: print "ROOT",
				if n.l:
					if not (n.l.p == n): 
						print "l parent/child mismatch", n.l.v 
						sys.exit()
					print "l", n.l.v,
					stack.append(n.l)
					if n.l.l and (n.l.l == n):
						print "ll cycle"
						sys.exit()
					if n.l.r and (n.l.r == n):
						print "lr cycle"
						sys.exit()
				if n.r:
					if not (n.r.p == n): 
						print "r parent/child mismatch", n.r.v 
						sys.exit()
					print "r", n.r.v, 
					stack.append(n.r)
					if n.r.l and (n.r.l == n):
						print "rl cycle"
						sys.exit()
					if n.r.r and (n.r.r == n):
						print "rr cycle"
						sys.exit()
				if not n.l and not n.r: 
					print "leaf",
					while n:
						print n.v, n.c,
						n = n.p
				print

	def is_valid_red_black_tree(self):
		print
		print "Checking tree validity..."
		# an empty tree is trivially a valid red-black tree
		if not self.root:
			return True
		else:
			valid = True
			# Test 2 - Root must always be black
			if not self.root.c == "Black":
				print "Error: Root is not black"
				return False
			stack = deque()
			stack.append(self.root)
			max_black_nodes_on_any_path = 0
			while stack:
				n = stack.pop()
				if (n.l and n.l.p and (not n.l.p == n)): 
					print "Error:", n.v, n.l.v, n.l.p.v, "parent l child mismatch"
					self.dfs()
					sys.exit()
				if (n.r and n.r.p and (not n.r.p == n)): 
					print "Error:", n.v, n.r.v, n.r.p.v, "parent r child mismatch"
					self.dfs()
					sys.exit()
				# Test 1 - Every node is either Red or Black
				if not ((n.c == "Black") or (n.c == "Red")):
					print "Error: A node exists that is neither red nor black"
					return False
				# Test 3 - There can never be two consecutive red nodes.
				if n.c == "Red":
					if (n.l and (n.l.c == "Red") or (n.r and n.r.c == "Red")):
						print n.v, "Error: Two consecutive red nodes exist on some path"
						return False
				if n.l: 
					if not n.l.v < n.v: 
						print "Error: left child is not less than its parent"
						return False
					stack.append(n.l)
				if n.r:
					if not n.r.v > n.v: 
						print "Error: right child is not greater than its parent"
						return False
					stack.append(n.r)
				# Test 4 - Every root to leaf path must have the same number of black nodes
				if not n.l or not n.r: 
					c = 0
					cur = n
					while cur:
						if cur.c == "Black": c += 1
						cur = cur.p
					print "Black nodes on path:", c
					if max_black_nodes_on_any_path == 0:
						max_black_nodes_on_any_path = c
					elif not c == max_black_nodes_on_any_path:
						print n.v, "Error: Not all paths have equal black nodes.", c, max_black_nodes_on_any_path
						valid = False
		if valid: 
			print "OK: Valid Red-Black tree."
			self.dfs()
		return valid	

	# Iterative delete ----------------------------------------------------------
	def rb_delete(self, n, v, p):
		# 1 perform standard delete
		print "Step 1"
		while n:
			if v == n.v:
				#print "found node", n.v,
				if n.l and n.r:
					#print "node has 2 children"
					s = n.r
					while s.l: s = s.l
					#print "swapping", n.v, s.v
					# when we swap values, do we also swap colors?
					n.v, s.v = s.v, n.v
					#n.c, s.c = s.c, n.c
					p = n
					n = n.r
					v = s.v
				else:
					#print "node has less than 2 children"
					# n is the node to be deleted - v
					# s is the successor (child that replaces the deleted node) - u
					s = None
					if n.l: 
						#print "successor is left child"
						s = n.l
					elif n.r: 
						#print "successor is right child"
						s = n.r

					if not p: 
						self.root = s
						if self.root: self.root.p = None
					elif p.l and (p.l.v == v): 
						p.l = s
						if p.l: p.l.p = p
					else: 
						p.r = s
						if p.r: p.r.p = p

					self.dfs()
					#if s: print s.v, "successor",
					#else: print "deleted node", n.v, "had no children",

					sc = self.get_color(s)
					nc = self.get_color(n)
					print nc, sc,
					# 2 simple case: either s or n is red
					if nc == "Red" or sc == "Red":
						print "2"
						if s: s.c = "Black"
						del n
						return
					# 3 both s and n are black
					elif nc == "Black" and sc == "Black":
						print "3",
						print "3.1",
						# 3.1 color s double black
						sc = "Double Black"
						if s: s.c = "Double Black"
						self.rb_rebalance_after_delete(s, sc, p)
						del n
						return
			elif v < n.v:
				p = n
				n = n.l
			elif v > n.v:
				p = n
				n = n.r

	def get_sibling(self, n, p):
		#if not n:
			#print "node does not exist", 
		#	return None
		if p:
			#print "node and parent exist",
			if p.l == n: 
				#print "found right sibling", n.p.l.v
				return p.r
			elif p.r == n: 
				#print "found left sibling", n.p.r.v
				return p.l
		else:
			print "parent does not exist",
			return None

	# unless you pass u's parent p, u might be null so you can't get u.p
	def rb_rebalance_after_delete(self, u, uc, p):
		if u == self.root: 
			print "arrived at root"
			# 3.3
			if u: 
				u.c = "Black"
				return
		if not uc == "Double Black": print "current node is not double black"
		# 3.2
		print "3.2",
		while (uc == "Double Black") and (not (u == self.root)):
			print uc, (u == self.root)
			if not u:
				print "u is null"
			else:
				print "u is", u.v
			s = self.get_sibling(u, p)
			if s: print s.v, "s"
			sc = self.get_color(s)
			slc = None
			src = None
			if s:
				print "sibling exists" 
				slc = self.get_color(s.l)
				src = self.get_color(s.r)
			else:
				print "sibling does not exist" 
				slc = "Black"
				src = "Black"
			#print uc, sc, slc, src,
			if sc == "Black":
				print "sibling is black"
				r = None
				if slc == "Red": 
					r = s.l
				elif src == "Red": 
					r = s.r
				# a
				if r:
					print "a"
					if p:
						if u == p.l:
							if r == r.p.l:
								print "i"
							elif r == r.p.r:
								print "ii"
						elif u == p.r:
							if r == r.p.r:
								print "iii"
							elif r == r.p.l:
								print "iv"
				# b
				else:
					print "b"
					# re-color the sibling and recur to the parent IF parent is black
					if s: 
						s.c = "Red"
						print "sibling changed to red"
					else:
						print "no sibling"
					if p:
						print "u has parent"
						if p.c == "Red": 
							p.c = "Black"
							# Don't recurse if parent color was red
							print "parent is red. changing to black"
							self.rb_rebalance_after_delete(p, p.c, p.p)
						else: 
							p.c = "Double Black"
							# Recurse if parent color was black
							print "parent is black. changing to double black"
							self.rb_rebalance_after_delete(p, p.c, p.p)
					elif u:
						print "no parent"
						print self.root.v, u.v
					else:
						print "u does not exist"
			#c
			elif sc == "Red":
				print "c"
				if p.l == s: 
					print "sibling is left child"
				if p.r == s: 
					print "sibling is right child"
					# rotate left
					# sibling takes the place of parent
					# parent becomes left child of sibling
					# right child of sibling becomes left child of parent
					s.c, p.c = p.c, s.c
					self.do_case_rr(u)		
					

			uc = "Black" # Bogus value to not have infinite loop
				
	


# Test -------------------------------------------------------------------------------------------------------

t = Red_Black_Tree()
#l = random.sample(xrange(16), 16)
l = [7,3,10,1,4,8,12,0,2,11,14]
l = [1,2,3,4,5,6,7]
l = [1,2,3,4,5,6]
print l
t.rb_ins_list(l)
t.dfs()
print

print t.is_valid_red_black_tree()

#random.shuffle(l)
t.dfs()
for v in l:
	print "deleting", v
	t.rb_delete(t.root, v, None)
	if not t.is_valid_red_black_tree(): sys.exit()
	#t.dfs()
t.dfs()

#TODO Implement delete


