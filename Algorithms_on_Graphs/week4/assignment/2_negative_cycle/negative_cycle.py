#Uses python3

import sys

def negative_cycle(g, c, s = 0):
	# change float("inf") to 10**10 > the comparison will 
	# be dist[u] vs dist[u] - 5, which is (inf vs inf - 5)
	# and no relaxation is made.
	distance = [10**10 for _ in range(len(adj))]
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
						return 1
	return 0
	
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
	print(negative_cycle(adj, cost))
