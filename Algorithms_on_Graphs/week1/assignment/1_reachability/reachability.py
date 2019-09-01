#Uses python3

import sys

def reach(adj, x, y):
	#write your code here
	print('{}, {}-{}'.format(adj, x, y))
	for i in range(len(adj)):
		try:
			adj[i][1]
			print('i ={}, adj[0]={}, adj[1]={}'.format(i, adj[i][0], adj[i][1]))
			continue
		except IndexError:
			pass
		try:
			adj[i][0]
			print('i ={}, adj[0]={}'.format(i, adj[i][0]))
			continue
		except IndexError:
			pass
	return 0

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
	print(reach(adj, x, y))
