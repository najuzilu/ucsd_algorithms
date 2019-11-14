#Uses python3

import sys

def explore(v, visited):
	visited[v] = True
	reachable[v] = 1
	for n in adj[v]:
		if visited[n] == False:
			explore(n, visited)

def negative_cycle(s):
	Q = []
	distance[s] = 0
	for iter_ in range(len(adj)):
		for i in range(len(adj)):
			for j in range(len(adj[i])):
				nodeVal = adj[i][j]
				costVal = cost[i][j]
				if distance[nodeVal] > distance[i] + costVal:
					if iter_ == len(adj) - 1:
						distance[nodeVal] = - float("inf")
						Q.append(nodeVal)
					else:
						distance[nodeVal] = distance[i] + costVal
	return Q

def explore_negative(v, visited):
	visited[v] = True
	for n in adj[v]:
		if visited[n] == False:
			shortest[n] = 0
			explore_negative(n, visited)

def shortet_paths(adj, cost, s, distance, reachable, shortest):
	# Find negative cycles and map as -inf
	Q = negative_cycle(s)

	# Convert all neg infinite values to shortest = 0
	for q in Q:
		shortest[q] = 0
		visited_negative = [False for _ in range(len(adj))]
		explore_negative(q, visited_negative)
	distance[s] = 0

	# Convert all non inifnite values to reachable = 1
	for i in range(len(distance)):
		item = distance[i]
		if item == float("inf"):
			reachable[i] = 0
		else:
			reachable[i] = 1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
	data = data[3 * m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((a, b), w) in edges:
		adj[a - 1].append(b - 1)
		cost[a - 1].append(w)
	s = data[0]
	s -= 1
	distance = [float("inf")] * n
	reachable = [0] * n
	shortest = [1] * n
	shortet_paths(adj, cost, s, distance, reachable, shortest)
	for x in range(n):
		if reachable[x] == 0:
			print('*')
		elif shortest[x] == 0:
			print('-')
		else:
			print(distance[x])