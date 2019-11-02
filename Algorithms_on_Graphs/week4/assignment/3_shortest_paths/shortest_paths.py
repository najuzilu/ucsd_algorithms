#Uses python3

import sys
import queue
import heapq
from heapq import heappush, heappop

"""
1) when the root is in a negative cycle and 2) when the root is reachable from a negative cycle. 
Remark: It is also necessary to exclude vertices to which lead the edges from the negative loop.

There are some ideas for code optimisation:
1. Process only those vertices (and associated edges) whose distances have been changed after relaxing.
2. Check for negative loops not at the end of the program, but during processing of the next vertex/edge. If there is a negative loop, then we exclude all loop-related vertices.


Use float('inf') instead of 10**19 (if you're using other languages make sure to change this as well)
Assign reachable[source] to 1
Relax all possible edge on V-1 iterations. If a node is relaxable, assign reachable[node] to 1
On Vth iteration, if a node is relaxable, put it in the queue (if it's not in the queue already), and note that you don't need to update the distance of that node either.
Run BFS for each nodes in the queue, after a node is taken out, you do some stuff with it (visited[node] = True, shortest[node] = 0 etc,.).
No need for v = parent[v], this solution still works like a charm.
"""

def negative_cycle(g, c, distance, s):
	L = []

	previous = [None for _ in range(len(adj))]
	distance[0] = 0

	for iter_ in range(len(g)):
		for i in range(len(g)):
			for j in range(len(g[i])):
				nodeVal = g[i][j]
				costVal = c[i][j]
				if distance[nodeVal] > distance[i] + costVal:
					distance[nodeVal] = distance[i] + costVal
					previous[nodeVal] = i
					if iter_ == len(g) - 1:
						heapq.heappush(L, nodeVal)
	return L, distance

def shortet_paths(adj, cost, s, distance, reachable, shortest):

	Q, distance = negative_cycle(adj, cost, distance, s)
	distance[s] = 0

	### Loop through negative cycles
	while Q:
		dequeue_node = heapq.heappop(Q)
		distance[dequeue_node] = -(10**19)
		shortest[dequeue_node] = 0
		for child in adj[dequeue_node]:
			if distance[child] > len(adj):
				heapq.heappush(Q, child)
				distance[child] = -(10**19)

	### Loop through visited path
	L = []
	heapq.heappush(L, s)
	reachable[s] = 1
	visited = [False for _ in range(len(adj))]

	while L:
		dequeue_node = heapq.heappop(L)
		visited[dequeue_node] = True
		for i in range(len(adj[dequeue_node])):
			child = adj[dequeue_node][i]
			if distance[child] > distance[dequeue_node] + cost[dequeue_node][i]:
				distance[child] = distance[dequeue_node] + cost[dequeue_node][i]
			if visited[child] == False:
				heapq.heappush(L, child)
				reachable[child] = 1

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
	distance = [10**19] * n
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

