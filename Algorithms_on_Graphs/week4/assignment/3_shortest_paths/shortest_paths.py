#Uses python3

import sys
import queue

def explore(v, g, visited, reach):
	visited[v] = True
	reach[v] = 1
	for n in g[v]:
		if visited[n] == False:
			explore(n, g, visited, reach)
	return reach

def negative_cycle(g, c, distance, s):
	L = []
	distance[s] = 0
	for iter_ in range(len(g)):
		for i in range(len(g)):
			for j in range(len(g[i])):
				nodeVal = g[i][j]
				costVal = c[i][j]
				if distance[nodeVal] > distance[i] + costVal:
					distance[nodeVal] = distance[i] + costVal
					### if in last iteration of verticies, 
					### then any negative node cycles append to heapq
					if iter_ == len(g) - 1:
						L.append(nodeVal)
	return L, distance

def exploreNeg(v, g, visited):
	visited[v] = True
	shortest[v] = 0
	distance[v] = - float("inf")
	for n in g[v]:
		# print('v={}, shortest[v]={}, distance[v]={}, shortest[n]={}, distance[n]={}'.format(v, shortest[v], distance[v], shortest[n], distance[n]))
		if visited[n] == False:
			exploreNeg(n, g, visited)

def shortet_paths(adj, cost, s, distance, reachable, shortest):
	### Step 1: vector named component to restore all connected
	### vertices explored from source s, and a function to get 
	### these elements. This vector contains the order information, 
	### which is significant for next moves.

	visited = [False for _ in range(len(adj))]
	reachable = explore(s, adj, visited, reachable)

	### Step 2: Do V-1 times B-F algorithm, from now on, there 
	### will be some changes if one vertex is in a negative cycle.
	Q, distance = negative_cycle(adj, cost, distance, s)

	### Step 3: 2 iterations based on the component order, 
	### look up all vertices in component, do relax function, 
	### but this time let the distance equals to -INF

	visitedNeg = [False for _ in range(len(adj))]
	for q in Q:
		if visitedNeg[q] == False:
			exploreNeg(q, adj, visitedNeg)

	distance[s] = 0
	# while Q:
	# 	dequeue_node = Q.pop(0)
	# 	shortest[dequeue_node] = 0
	# 	for i in range(len(adj[dequeue_node])):
	# 		child = adj[dequeue_node][i]
	# 		if distance[child] > distance[dequeue_node] + cost[dequeue_node][i]:
	# 			distance[child] = -(float("inf"))
	# 			# shortest[child] = 0
	# 			Q.append(child)


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
	# distance = [10**19] * n
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