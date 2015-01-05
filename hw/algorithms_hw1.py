# module 1
"""
Module and Example Graphs
"""

EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])} 

EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}

GRAPH0 = {0: set([1]),
          1: set([2]),
          2: set([3]),
          3: set([0])}

GRAPH1 = {0: set([]),
          1: set([0]),
          2: set([0]),
          3: set([0]),
          4: set([0])}

GRAPH2 = {0: set([1, 2, 3, 4]),
          1: set([]),
          2: set([]),
          3: set([]),
          4: set([])}

GRAPH3 = {0: set([1, 2, 3, 4]),
          1: set([0, 2, 3, 4]),
          2: set([0, 1, 3, 4]),
          3: set([0, 1, 2, 4]),
          4: set([0, 1, 2, 3])}

GRAPH4 = {"dog": set(["cat"]),
          "cat": set(["dog"]),
          "monkey": set(["banana"]),
          "banana": set([])}

GRAPH5 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([4, 6, 8]),
          4: set([3, 5, 7]),
          5: set([6, 8]),
          6: set([5, 7]),
          7: set([8]),
          8: set([7])}

GRAPH6 = {1: set([2, 5]),
          2: set([1, 7]),
          3: set([4, 6, 9]),
          4: set([6]),
          5: set([2, 7]),
          6: set([4, 9]),
          7: set([1, 5]),
          9: set([3, 4])}

GRAPH7 = {0: set([1, 2, 3, 4]), 
          1: set([0, 2, 3, 4]), 
          2: set([0, 1, 3, 4]), 
          3: set([0, 1, 2, 4]), 
          4: set([0, 1, 2, 3]), 
          5: set([2, 3, 4]), 
          6: set([0, 1, 4]), 
          7: set([0, 1, 2, 3]), 
          8: set([0, 1, 4, 7]), 
          9: set([2, 4]), 
          10: set([1, 2, 4]), 
          11: set([1, 3, 4, 7]), 
          12: set([0, 2, 3]), 
          13: set([0, 2, 4, 10]), 
          14: set([0, 2, 3, 4, 13])}

GRAPH8 = {0: set([1, 2]), 
          1: set([0, 2]), 
          2: set([0, 1]), 
          3: set([0]), 
          4: set([1, 2]), 
          5: set([0, 2]), 
          6: set([1, 2, 4]), 
          7: set([0, 3]), 
          8: set([0, 1]), 
          9: set([0, 7]), 
          10: set([0]), 
          11: set([0, 1, 3]), 
          12: set([0, 4, 7]), 
          13: set([0, 5]), 
          14: set([0, 1, 8]), 
          15: set([0, 1, 3]), 
          16: set([1, 14, 6]), 
          17: set([0, 8]), 
          18: set([0, 1]), 
          19: set([0, 1, 17])}

GRAPH9 = {0: set([1, 2, 3, 4, 5, 6]),
          1: set([0, 2, 3, 4, 5, 6]),
          2: set([0, 1, 3, 4, 5, 6]),
          3: set([0, 1, 2, 4, 5, 6]),
          4: set([0, 1, 2, 3, 5, 6]),
          5: set([0, 1, 2, 3, 4, 6]),
          6: set([0, 1, 2, 3, 4, 5]),
          7: set([1, 3, 4, 6]),
          8: set([0, 3, 4, 5, 6]),
          9: set([0, 5, 6, 7]),
          10: set([1, 2, 4, 9]),
          11: set([1, 2, 4, 6]),
          12: set([0, 2, 4, 6]),
          13: set([1, 2, 4, 5]),
          14: set([0, 1, 4, 6]),
          15: set([1, 4, 5, 6]),
          16: set([0, 1, 2, 4, 6]),
          17: set([0, 1, 2, 4, 5, 6]),
          18: set([2, 4, 5, 6, 13]),
          19: set([1, 2, 3, 5, 6]),
          20: set([0, 1, 2, 4, 5]),
          21: set([1, 2, 4, 5, 15]),
          22: set([0, 9, 4, 5, 13]),
          23: set([0, 1, 2, 3, 5, 20]),
          24: set([0, 1, 2, 3, 4, 5, 6]),
          25: set([0, 1, 2, 4, 5]),
          26: set([1, 2, 4, 5, 10, 22]),
          27: set([1, 2, 3, 5, 6]),
          28: set([0, 1, 3, 5]),
          29: set([2, 26, 4, 5, 6]),
          30: set([0, 2, 4, 6, 7]),
          31: set([20, 4, 21, 6]),
          32: set([1, 2, 4, 20, 28]),
          33: set([0, 4, 5, 6, 8, 22]),
          34: set([0, 2, 4, 5, 15]),
          35: set([1, 2, 5, 6, 9, 28]),
          36: set([24, 2, 3, 4, 6]),
          37: set([0, 1, 2, 4, 6, 10, 29]),
          38: set([0, 24, 11, 5, 6]),
          39: set([0, 1, 22, 6, 17]),
          40: set([0, 1, 2, 3, 5, 15]),
          41: set([11, 2, 3, 5, 6]),
          42: set([16, 1, 2, 5]),
          43: set([0, 1, 2, 4, 22]),
          44: set([32, 3, 6, 24, 27, 29]),
          45: set([1, 2, 4, 5, 16, 18, 37]),
          46: set([1, 5, 6, 7, 8, 12, 14]),
          47: set([8, 20, 2, 4]),
          48: set([0, 16, 2, 5, 14]),
          49: set([2, 21, 18, 6, 15])}




#python homework
def make_complete_graph(num_nodes):
     """
     Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes. A complete graph contains all possible edges subject to the restriction that self-loops are not allowed. The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive. Otherwise, the function returns a dictionary corresponding to the empty graph.
     """
     node_set = {node_set:set([]) for node_set in range(num_nodes)}
     for node in node_set:
	    node_set[node]=set([new_node for new_node in node_set if new_node!=node])
     return node_set

def compute_in_degrees(digraph):
	""" 
	Takes a directed graph digraph 
	(represented as a dictionary) and 
	computes the in-degrees for the
	 nodes in the graph. The function
	 should return a dictionary with
	 the same set of keys (nodes) as
	 digraph whose corresponding values
	 are the number of edges whose head
	 matches a particular node.
	"""
	indegree = {degree:0 for degree in digraph}
	for key in indegree:
		for degree in digraph[key]:
			if degree!=key:
				indegree[degree]+=1
	return indegree

def in_degree_distribution(digraph):
     """
     Takes a directed graph digraph (represented as a 
     dictionary) and computes the unnormalized 
     distribution of the in-degrees of the graph. 
     The function should return a dictionary whose 
     keys correspond to in-degrees of nodes in the 
     graph. The value associated with each 
     particular in-degree is the number of 
     nodes with that in-degree. In-degrees 
     with no corresponding nodes in the graph 
     are not included in the dictionary.
     """
     distribution={}
     indegrees = compute_in_degrees(digraph)
     for value in indegrees.values():
          if value in distribution:
               distribution[value]+=1
          else: distribution[value]=1
     return distribution

def normalize_distribution(distribution):
     total = sum(distribution.values())
     distr = {}
     for key,value in distribution.items():
          distr[key] = (value+0.0)/total
     return distr

# EXAMPLES
#print make_complete_graph(1)
digraph = GRAPH6
#print digraph
#print compute_in_degrees(digraph)
#print in_degree_distribution(digraph)
#print normalize_distribution(in_degree_distribution(digraph))

# PART 2
# APPLICATION
# http://www.codeskulptor.org/#user37_kNdjbdwAPt_20.py


import random
def ER(n, p):
     """
     output a graph g = (v,e) where g member of G(n,p)
     """
     v = range(n)
     e = []
     for i in v: 
          for j in v: 
               if i!=j:
                    a= random.random()
                    if a<p:
                         e.append((i,j))

     return (v,e)

def ER_directed(n, p):
     """
     output a DIRECTED graph g = (v,e) where g member of G(n,p)
     """
     v = range(n)
     e = []
     for i in v: 
          for j in v: 
                    a= random.random()
                    if a<p:
                         e.append((i,j))

     return (v,e)

for p in [x/100.0 for x in range(0,100,10)]:
     print len(ER_directed(10, p)[1])
