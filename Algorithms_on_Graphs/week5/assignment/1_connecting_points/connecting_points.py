#Uses python3
import sys
import math
# from collections import OrderedDict

"""
1. use disjoint set data structures
2. initially each vertex lies in a separate set
3. each set is the set of vetices of a connected component
4. to check whether the current edge {u, v} produces a cycle, we check whether u and v belong to the same set

- disjoint sets: A   B   C   D   E   F
- 1st lighest edge is A-E; we check to see if A or E lie in different connected components (findOf(A) and findOf(E)) >> add edge to current solution >> update data structure: A,E  B   C   D   F
- next lightest edge is C-F: we check to see if C or F lie in different connected components (findOf(C) and findOf(F)) >> add edge to current solution >> update data structure (Union(C,F)): A,E  B   C,F  D
- next lightest edge is A-D: we check to see if A or D lie in different connected components (findOf(A) and findOf(D)) >> add edge to current solution >> update data structure: A,E,D  B   C,F  D
- next lightest edge is D-E: we check to see if D or E lie in different connected components (findOf(D) and findOf(E)) >> skip
- next lightest edge is _-_: we check to see if _ or _ lie in different connected components (findOf(_) and findOf(_)) >> add edge to current solution >> update data structure: A,E  B   C,F  D
...

Kurskal(G):
for all u in V:
	MakeSet(v)
X <- empty set
sort the edges E by weight
for all {u, v} in E in non decreasing weight order:
	if Find(u) != Find(v):
		add {u, v} to X
		Union(u, v)
return X

"""

def create_all_edges(x, y):
	"""
		Sort edges E by weight.
	"""
	dict_edges = {}
	for i in range(len(x)):
		print('looping through x with i =', i)
		dict_edges['{}{}'.format(x[i],y[i])] = math.sqrt(x[i]**2 + y[i]**2)
	sorted_dict = sorted(dict_edges.items(), key=lambda kv: kv[1])
	return sorted_dict

def minimum_distance(x, y):
	result = 0.0

	i = 0
	copy_edges = [(x[i], y[i]) for i in range(len(x))]
	edges_exist = []

	while len(copy_edges) > 1:
		print('Total copy_edges = ' , copy_edges ,'\nlooping through current point: ', copy_edges[i])

		# dict_edges needs to be reset at every iteration
		dict_edges = {}
		# add current location to dict_edges
		edges_exist.append(copy_edges[i]) 			# removes edge distance 0 from comparison
		
		# calculate distances from this point if they're not in edges_exist
		for j in range(len(copy_edges)): # problem
			if copy_edges[i] != copy_edges[j]: # distance is not 0 // copy_edges[j] not in edges_exist and 
				dict_edges[copy_edges[j]] = math.sqrt( (copy_edges[i][0] - copy_edges[j][0])**2 + (copy_edges[i][1] - copy_edges[j][1])**2 )

		# sort dict_edges
		sorted_dict = sorted(dict_edges.items(), key=lambda kv: kv[1])
		
		print("Optimal distance from {} to {} is {}".format(copy_edges[i], sorted_dict[0][0], sorted_dict[0][1]))
		result += sorted_dict[0][1]

		# remove from copy_edge
		copy_edges.pop(i)

		# update i value
		i = copy_edges.index(sorted_dict[0][0])
		print('\n')

	return result


if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	print("{0:.9f}".format(minimum_distance(x, y)))
