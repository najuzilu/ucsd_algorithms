#Uses python3

import sys

sys.setrecursionlimit(200000)

def reverse_graph(G):
	"""
		Reversed the current graph and returns it
	"""
	G_R = [ [] for _ in range(len(G))] # reversed graph
	for index in range(len(G)):
		for element in G[index]:
			G_R[element].append(index)
	return G_R

def explore(node, visited, previous, cc_num):
	"""
		Explores the node and updates the pre/post-order numbers
	"""
	visited[node] = True
	# order_number[node][0] = cc_num # adds preorder number
	order_number[node][0] = node # adds node number instead of preorder number
	cc_num += 1
	for child in adj[node]:
		if visited[child] == False:
			cc_num = explore(child, visited, node, cc_num)
	order_number[node][1] = cc_num
	cc_num += 1
	return cc_num

def DFS(g):
	"""
		Run DFS on graph and updates pre/post-order numbers
		Preorder numbers are not neccessary but wanted to
		implement either way.
	"""
	global order_number
	visited = [False for _ in range(len(adj))]
	order_number = [[None, None] for _ in range(len(adj))]
	cc_num = 1
	for i in range(len(adj)):
		if visited[i] == False:
			cc_num = explore(i, visited, i, cc_num)

def explore_scc(node, previous, adj, count):
	scc_visited[node] = True
	for child in adj[node]:
		if scc_visited[child] == False:
			count = explore_scc(child, node, adj, count)
	
def number_of_strongly_connected_components(adj):
	global scc_visited
	result = 0
	scc_visited = [False for _ in range(len(adj))]

	adj_reversed = reverse_graph(adj)
	DFS(adj_reversed)
	order_number.sort(key=lambda x: x[1], reverse = True) # sort order_number

	for i in range(len(adj_reversed)):
		node_index, max_value = order_number[i][0], order_number[i][1] # sort in reverse the postorder numbers
		if scc_visited[node_index] == False:
			result += 1
			explore_scc(node_index, node_index, adj_reversed, result)
	return result

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
	adj = [[] for _ in range(n)]
	for (a, b) in edges:
		adj[a - 1].append(b - 1)
	print(number_of_strongly_connected_components(adj))
