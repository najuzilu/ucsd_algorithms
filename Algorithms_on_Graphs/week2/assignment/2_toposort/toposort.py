#Uses python3

import sys

def explore(node, visited, previous):
	visited[node] = True

	for child in adj[node]:
		if visited[child] == False:
			explore(child, visited, previous)

	ranked.insert(0, node)
	if adj[node] == []:
		if previous != node:
			adj[previous].remove(node)

def DFS(g):
	visited = [False for _ in range(len(adj))]
	for i in range(len(adj)):
		if visited[i] == False:
			explore(i, visited, i)
	
def toposort(adj):
	global ranked
	ranked = []
	DFS(adj)
	return ranked


if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
	order = toposort(adj)
	for x in order:
		print(x + 1, end=' ')

