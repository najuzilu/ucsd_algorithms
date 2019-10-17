#Uses python3

import sys
import queue

def distance(adj, s, t):
	L = queue.Queue(maxsize = len(adj)) # initialize queue
	distance = [len(adj) for _ in range(len(adj))] # initialize distance list
	distance[s] = 0 # set starting node distance to 0
	L.put(s) # add starting node to queue

	while not L.empty(): # while queue is not empty
		dequeue_node = L.get() # take the first element
		for child in adj[dequeue_node]:
			if distance[child] == len(adj):
				L.put(child)
				distance[child] = distance[dequeue_node] + 1

	if distance[t] < len(adj):
		return distance[t]
	else:
		return -1

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
	s, t = data[2 * m] - 1, data[2 * m + 1] - 1
	print(distance(adj, s, t))
