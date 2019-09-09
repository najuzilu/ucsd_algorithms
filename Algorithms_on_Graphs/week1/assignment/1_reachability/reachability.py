#Uses python3

import sys

def reach(adj, x, y, disc):
	disc.append(x)
	count = 0 # count paths
	for node in adj[x]:
		# print('looping through node', node)
		if node == y:
			count += 1
		else:
			# not y
			if node in disc:
				pass
			else:
				disc.append(node)
				count += reach(adj, node, y, disc)
	return count

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	x, y = data[2 * m:]
	adj = [[] for _ in range(n)]
	x, y = x - 1, y - 1
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
		adj[b - 1].append(a - 1)
	discovered_nodes = []
	no_paths = reach(adj, x, y, discovered_nodes)
	if no_paths == 0:
		print(no_paths)
	else:
		print(1)
