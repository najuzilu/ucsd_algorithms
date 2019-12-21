#Uses python3
import sys
import math

def union(u, v, set_dist):
	v_index = find(v, set_dist)
	u_index = find(u, set_dist)

	for item in set_dist[v_index]:
		set_dist[u_index].append(item)

	set_dist.pop(v_index)
	return set_dist

def find(u, set_dist):
	for i in range(len(set_dist)):
		if u in set_dist[i]:
			return i
	return -1

def calculate_distances(x, y):
	all_sets = []
	for i in range(len(x)):
		current_point = (x[i], y[i])
		for j in range(i+1, len(x)): # skip where x[i],y[i] same as x[j],y[j]
			distance = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
			all_sets.append((distance,((x[i],y[i]),(x[j],y[j]))))
	return all_sets

def clustering(x, y, k):
	result = []
	disjoint_sets = [[(x[i], y[i])] for i in range(len(x))]
	#  calculate all disjoin sets with distance
	distances = calculate_distances(x, y)
	# sort edges by distance
	sorted_dist = sorted(distances, key = lambda x: x[0])
	for pair in sorted_dist:
		u = pair[1][0]
		v = pair[1][1]
		
		if find(u, disjoint_sets) != find(v, disjoint_sets):
			# add {u,v} to x
			result.append(pair[0])
			# union(u, v)
			disjoint_sets = union(u, v, disjoint_sets)

	return result[len(result) - (k-1)]

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	data = data[1:]
	x = data[0:2 * n:2]
	y = data[1:2 * n:2]
	data = data[2 * n:]
	k = data[0]
	print("{0:.9f}".format(clustering(x, y, k)))
