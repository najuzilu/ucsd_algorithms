#Uses python3

import sys
import queue

def distance(adj, s = 0):
	L = queue.Queue(maxsize = len(adj)) # initialize queue
	distance = [len(adj) for _ in range(len(adj))] # initialize distance list
	color = [None for _ in range(len(adj))] # initialize previous list
	distance[s] = 0 # set starting node distance to 0
	color[0] = 'white'
	L.put(s) # add starting node to queue

	while not L.empty(): # while queue is not empty
		dequeue_node = L.get() # take the first element
		for child in adj[dequeue_node]:
			if color[child] == color[dequeue_node]:
				return 0
			if distance[child] == len(adj):
				L.put(child)
				distance[child] = distance[dequeue_node] + 1
				if color[child] == None:
					if color[dequeue_node] == 'black':
						color[child] = 'white'
					else:
						color[child] = 'black'
	return 1

def bipartite(adj):
	return distance(adj)

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
	print(bipartite(adj))
