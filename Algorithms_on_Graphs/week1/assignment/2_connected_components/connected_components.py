#Uses python3

import sys

def explore(v, visited, cc_coef):
	visited[v] = True
	if cc_coef not in cc_array:
		cc_array.append(cc_coef)
	for node in adj[v]:
		if visited[node] == False:
			explore(node, visited, cc_coef)


def number_of_components(adj):
	global cc_array
	cc_array = [] # connected component array

	visited = [False for _ in range(len(adj))]
	cc_coef = 1 # connected compononent number
	for i in range(len(adj)):
		if visited[i] == False:
			explore(i, visited, cc_coef)
			cc_coef += 1
	return len(cc_array)


if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
		adj[b - 1].append(a - 1)
	print(number_of_components(adj))
