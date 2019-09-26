#Uses python3

import sys

def explore(v, visited, i):
	visited[v] = True
	for node in adj[v]:
		if visited[node] == False:
			explore(node, visited, i)
		if node == i:
			global result
			result = 1

def acyclic(adj):
	for i in range(len(adj)):
		visited = [False for _ in range(len(adj))]
		if visited[i] == False:
			explore(i, visited, i)
			if result == 1:
				return 1
	return 0

if __name__ == '__main__':
	result = 0
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
	print(acyclic(adj))
