#! /usr/bin/env python

# Graphs
# can be undirected or directed
# cyclic or acyclic
# weighted or unweighted
# simple (no self loops or multi-edges) or non-simple
# sparse (closer to 1 or n), dense (closer to n^2), or complete (all n^2 edges present)

# graphs have a set of nodes (or vertices - I prefer the term node) and a set edges connecting two nodes

# adjacent: two nodes have at least one edge that connects them
# walk: sequence of adjacent nodes
# path: a walk with no repeated nodes
# reachable: some path exists between two nodes

# subgraph: subset of nodes and edges of some other graph
# component (or connected component): a subgraph in which every node is reachable from every other node
# graphs can have multiple separate components, like islands each having separate road networks 

# undirected graph terminology:
# endpoints, neighbors (other nodes sharing an edge with this node), degree (how many neighbors the node has)
# in u-v, u and v are endpoints. they are also neighbors.
# connected: every node is reachable from every other node

# directed graph terminology:
# predecessor (in-neighbor) - in u->v, u is a predecessor of v
# successor (out-neighbor) - in u->v, v is a successor of u
# in-degree - number of predecessors adjacent to this node
# out-degree - number of successors adjacent to this node
# strongly connected: every node is reachable from every other node
# directed walk: sequence of directed edges where the head of each edge is the tail of the next
# directed path: a directed walk where no node is repeated
# reachable: a directed path exists from a given node to another node

import random
from collections import defaultdict
from collections import deque
import sys
import math

class Node():
	def __init__(self):
		self.visited = False
		self.label = None
		self.xy = (0,0)

class Graph():
	def __init__(self, is_directed=True, is_simple=True, is_weighted=True):
		self.is_directed = is_directed
		self.is_simple = is_simple
		self.is_weighted = is_weighted
		self.e = defaultdict(dict)
		self.n = defaultdict(dict)
		self.visited = defaultdict(lambda: False)

	def add_edge(self, u, v, w=0):
		if self.is_simple and (u == v):
			return
		if self.is_directed: 
			self.add_directed_edge(u, v, w)
		else: 
			self.add_undirected_edge(u, v, w)

	def add_undirected_edge(self, u, v, w=0):
		self.add_directed_edge(u, v, w)
		self.add_directed_edge(v, u, w)
	
	def add_directed_edge(self, u, v, w=0):
		self.e[u][v] = w

	def add_node(self, u):
		if not self.n[u]: 
			self.n[u] = Node()
			self.n[u].visited = False

	def is_reachable(self, u, v, visited):
		if not u in visited:
			visited.append(u)
			if u == v:
				return visited 
			else:
				for t in self.e[u].keys():
					if not t in visited:
						if self.is_reachable(t, v, visited): 
							return visited
		return False

	# was not optimal - added memoing to skip processed paths
	# for undirected graphs, you don't need to check path v,u if u,v was already checked
	# u, u is trivially true
	# also, all sub-paths of a discovered path don't need to be checked again.

	# after fixing this, instead of doing n^2 path checks, it only needs to do less than n path checks!
	def is_connected(self):
		checked = defaultdict(lambda: False) 
		for u in self.e.keys():
			for v in self.e.keys():
				if not checked[(u, v)]:
					path = self.is_reachable(u, v, [])
					if not path:
						return False
					else:
						for x in path:
							for y in path:
								checked[(x,y)] = True
								checked[(y,x)] = True
				else: 
					print "already checked", u, v
					if len(checked.keys()) == len(self.e.keys()) * len(self.e.keys()):
						print "Everything was already checked" 
						return True
		return True

	# max recursion depth will be exceeded if input size is 1000 or more
	def dfs(self, n=1):
		self.visited[n] = True
		for neighbor in self.e[n].keys():
			if not self.visited[neighbor]:
				self.dfs(neighbor)
	
	# every time you double the input size, the run time takes about 5-6x longer
	# at 5000, it takes about ~50s
	# once you go to 6400, it shoots up to ~10 minutes, probably due to memory swapping to disk 
	def dfsi(self, e, n=1):
		self.set_all_nodes_to_unvisited()
		stack = []
		stack_member = defaultdict(lambda: False)
		stack.append(n)
		# this reduces the lookup time to check if each item is in a stack from O(n) to O(1)
		stack_member[n] = True
		while(stack):
			n = stack.pop()
			# this allows us to find out if a random node was visited in O(1) instead of O(n)
			self.visited[n] = True
			stack_member[n] = False
			for neighbor in e[n].keys():
				if (not stack_member[neighbor]) and (not self.visited[neighbor]):
					stack.append(neighbor)
					stack_member[neighbor] = True

	# will only visit connected nodes
	def bfs(self, n=1):
		self.set_all_nodes_to_unvisited()
		# deques are faster than lists in python for appends and pops
		q = deque()
		q_member = defaultdict(lambda: False)
		q.append(n)
		q_member[n] = True
		while(q):
			# by using popleft, the deque behaves as a queue
			n = q.popleft()
			# this allows us to find out if a random node was visited in O(1) instead of O(n)
			self.visited[n] = True
			q_member[n] = False
			for neighbor in self.e[n].keys():
				if (not q_member[neighbor]) and (not self.visited[neighbor]):
					q.append(neighbor)
					q_member[neighbor] = True
			
	def is_connected2(self):
		self.dfsi(self.e)
		return all(v == True for v in self.visited.values())

	def is_inverse_connected(self):
		inverse_graph = self.invert_edges(self.e)
		self.dfsi(inverse_graph)
		return all(v == True for v in self.visited.values())

	def is_strongly_connected(self):
		for u in self.e.keys():
			for v in self.e.keys():
				if not self.is_reachable(u, v, []):
					return False
		return True

	def invert_edges(self, e):
		i = defaultdict(dict)
		for u in e:
			for v in e[u]:
				i[v][u] = w
		return i

	def set_all_nodes_to_unvisited(self):
		self.visited.clear()
		for x in self.n: self.visited[x] = False

	# https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/
	# A graph is strongly connected if 
	# every node is reachable from a given node
	# and every node can reach that node
	def kosaraju(self):
		if not self.is_connected2(): 
			return False
		else:
			# check inverse of graph
			return self.is_inverse_connected()


	# Implementation of Prim's algorithm
	# for finding a minimum spanning tree in a weighted graph
	def prim(self):
		inMST = defaultdict(lambda: False)
		d = defaultdict(lambda: sys.maxint)
		p = defaultdict(lambda: None)
		d[1] = 0
		for n in range(len(self.n)):
			u = self.get_nearest_node(d, inMST)
			if not u: break
			inMST[u] = True
			for v in self.e[u].keys():
				# This is the main difference from dijkstra's algorithm:
				# In prim's algorithm, 
				# the minimum spanning tree is greedily constructed from
				# next individual edge of minimum weight
				# whereas in dijkstras, shortest path tree comes from
				# path of least total weight
				if (self.e[u][v] > 0) and (not inMST[v]) and (d[v] > self.e[u][v]):
					d[v] = self.e[u][v]
					p[v] = u
		self.printMST(p)

	def printMST(self, p):
		print "\nPrim's minimum spanning tree:"
		for i in self.e.keys():
			if i and p[i]:
				print p[i], "->", i, "  \t",
				print self.e[p[i]][i]

	# Implementation of Dijkstra's algorithm 
	# for finding shortest paths from an arbitrary node to all other nodes in a weighted graph
	def dijkstra(self, src, dest):
		steps = 0
		# Initially, nothing is in the shortest path tree
		# And all nodes are undiscovered - infinitely far away
		inSPT = defaultdict(lambda: False)
		d = defaultdict(lambda: sys.maxint)
		p = defaultdict(lambda: [])
		# The source node has a distance of zero
		d[src] = 0
		p[src].append(src)
		# We repeat the discovery process once for each node
		for n in range(len(self.n)):
			# Find the next nearest node
			u = self.get_nearest_node(d, inSPT)
			steps += 1
			if u == dest: 
				print "Steps:", steps, "\t",
				break
			if not u: break
			# And place it as a fixed node in the shortest path tree
			# This is a "greedy" algorithm because always choosing the nearest node first turns out to be optimal
			inSPT[u] = True
			# Then we update all of the distances 
			# for all neighbors (v) of u 
			for v in self.e[u].keys():
				# if there is an edge from u to v with positive weight, 
				# and v is not already in the shortest path tree,
				# and the current distance to v is greater than the new path found through u
				if (self.e[u][v] > 0) and (not inSPT[v]) and (d[v] > d[u] + self.e[u][v]):
					# then we can shorten the path to v
					# the shortest path to v now goes through u
					d[v] = d[u] + self.e[u][v]
					# you need to assign a copy of the list to work
					# copy path src->u and append u->v
					p[v] = p[u][:]
					p[v].append(v)

		# Print results
		n = dest
		#print "Dijkstra's shortest paths from", src
		if p[n]:
			print "Goal:", src, dest, "\tDist:", d[n], "\tPath:",
			prev = None 
			for step in p[n][:-1]:
				prev = step 
				print step, "->",
			print p[n][-1]
		else:
			print "No path to", dest

	def get_nearest_node(self, d, inSPT):
		# to start with, there is no nearest node
		nearest = None
		# and the shortest distance to the nearest node is infinite
		m = sys.maxint
		# for each node in the graph, check its distance
		for n in self.n:
			# if the distance to this node is shorter than the shortest distance to any other node found so far
			if (d[n] < m) and (not inSPT[n]):
				# then update the shortest distance to be the distance to this node
				m = d[n]
				# and remember this node as the new nearest node
				nearest = n
		# return the nearest node found after checking every node
		return nearest

	# TODO:  Add obstacles
	def a_star(self, src, dest, h):
		steps = 0
		inSPT = defaultdict(lambda: False)
		f = defaultdict(lambda: sys.maxint)
		# g is the distance so far between start and current node
		g = defaultdict(lambda: sys.maxint)
		p = defaultdict(lambda: [])
		f[src] = 0
		g[src] = 0
		# 1
		p[src].append(src)
		# 2
		for n in range(len(self.n)):
			# A - u is the current square
			u = self.get_nearest_node(f, inSPT)
			steps += 1
			if u == dest: 
				print "Steps:", steps, "\t",
				break
			if not u: break
			# B
			inSPT[u] = True
			# C
			for v in self.e[u].keys():
				# h is the heuristic distance between current and dest
				if (self.e[u][v] > 0) and (not inSPT[v]) and (g[v] > g[u] + h(u, dest)):
					g[v] = g[u] + self.e[u][v]
					f[v] = g[v] + h(v, dest)
					p[v] = p[u][:]
					p[v].append(v)

		n = dest
		if p[n]:
			#print "A* shortest path from", src, "to destination", n
			print "Goal:", src, dest, "\tDist:", g[n], "\tPath:",
			prev = None 
			for step in p[n][:-1]:
				prev = step 
				print step, "->",
			print p[n][-1]
		else:
			print "No path to", dest

	# heuristic function:
	# calculate the straight cartesian distance between the 2 points
	# IE: the shortest path would be a straight line if such an edge exists
	def h1(self, u, v):
		dx = (g.n[u].xy[0] - g.n[v].xy[0])
		dy = (g.n[u].xy[1] - g.n[v].xy[1])
		w = math.sqrt((dx**2) + (dy**2))
		return w

	def h2(self, u, v):
		return 0
		

min_nodes = 2000
max_nodes = 2000

min_weight = 100
max_weight = 10000

# populate a random graph with nodes and edges
g = Graph(is_directed=True)
# generate a random number of nodes

nodes = range(1, random.randint(min_nodes, max_nodes) + 1)
for u in nodes:
	g.add_node(u)
	g.n[u].xy = (random.randint(0,1000), random.randint(0,1000))

for u in nodes:
	# generate some random subset of all nodes as neighbors to this node
	neighbors = random.sample(nodes, random.randint(0, len(nodes)))
	#neighbors = neighbors[:random.randint(1,10)]
	#print len(neighbors)
	#neighbors = nodes
	for v in neighbors:
		if g.is_simple and (u == v): continue
		if g.is_weighted:
			#w = random.randint(min_weight, max_weight)
			w = g.h1(u,v)
			g.add_edge(u, v, w)
			#print g.n[u].xy, "->", g.n[v].xy, g.e[u][v]
		else:
			g.add_edge(u, v)


#g.dijkstra()
#g.prim()
#g.bfs()

#src = 1
# pick 2 arbitrary points in a graph and find the shortest path between them
src = random.randint(1, len(nodes))
dest = random.randint(1, len(nodes))
print "A*:      \t",
g.a_star(src, dest, g.h1)
print "Dijkstra:\t",
g.dijkstra(src, dest)

#if g.is_directed: print "K:", g.kosaraju()
#else: print "D:", g.is_connected2()
