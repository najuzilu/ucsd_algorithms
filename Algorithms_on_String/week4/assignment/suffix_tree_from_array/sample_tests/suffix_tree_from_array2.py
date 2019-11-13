# python3
import sys

class suffix_tree_node(object):
	def __init__(self, children, parent, string_depth, edge_start, edge_end):
		self.children = children
		self.parent = parent
		self.string_depth = string_depth
		self.edge_start = edge_start
		self.edge_end = edge_end

def create_new_leaf2(node, s, suffix):
	"""
		Create new leaf with the following info:
			children = {}
			parent = node
			string_depth = len(s) - suffix
			edge_start = suffix + node.string_depth
			edge_end = len(s)
		Update node.children[s[lead.edge_start]] = leaf
		Return leaf
	"""
	leaf = suffix_tree_node({}, node, len(s)-suffix, suffix + node.string_depth, len(s))
	node.children[s[leaf.edge_start]] = leaf
	return leaf

def break_edge2(node, s, start, offset):
	start_char = s[start]
	mid_char = s[start + offset]
	mid_node = suffix_tree_node({}, node, node.string_depth + offset, start, start+offset-1)
	mid_node.children[mid_char] = node.children[start_char]
	node.children[start_char].parent = mid_node
	node.children[start_char].edge_start += offset
	node.children[start_char] = mid_node
	return mid_node

def suffix_array_to_suffix_tree2(sa, lcp, text):
	"""
		Inputs as follow:
			sa - suffix_array
			lcp - longest common prefix array
			text - actual text

	"""
	root = suffix_tree_node({}, None, 0, -1, -1)
	lcp_prev = 0
	cur_node = root

	for i in range(len(text)):
		suffix = sa[i]

		while cur_node.string_depth > lcp_prev:
			cur_node = cur_node.parent

		if cur_node.string_depth == lcp_prev:
			cur_node = create_new_leaf(cur_node, text, suffix)
		else:
			edge_start = sa[i-1] + cur_node.string_depth
			offset = lcp_prev - cur_node.string_depth
			mid_node = break_edge(cur_node, text, edge_start, offset)
			cur_node = create_new_leaf(mid_node, text, suffix)

		if i < len(text)-1:
			lcp_prev = lcp[i]
	return root

def create_new_leaf(node, s, suffix):
	"""
		node => parent node
		s => text
		suffix => sa[i]

	# print("children_array", children_array)
	# print("parent_array",parent_array)
	# print("string_depth_array",string_depth_array)
	# print("edge_start_array",edge_start_array)
	# print("edge_end_array",edge_end_array)
	# print("TREE=", tree)

	"""
	leaf = suffix + 1 # add one cuz suffix 0 is root node in tree

	children_array[leaf] = {}
	parent_array[leaf] = node
	string_depth_array[leaf] = len(s) - suffix
	edge_start_array[leaf] = suffix + string_depth_array[node]
	edge_end_array[leaf] = len(s)

	# Add as child of node
	if len(children_array[node]) > 0:
		children_array[node][s[edge_start_array[leaf]]] = leaf
	else:
		children_array[node] = {s[edge_start_array[leaf]] : leaf}
	
	# Add to tree
	if len(tree[node]) > 0:
		tree[node][s[edge_start_array[leaf]]] = leaf
	else:
		tree[node] = {s[edge_start_array[leaf]] : leaf}
	return leaf

def break_edge(node, s, start, offset):
	start_char = s[start]
	mid_char = s[start + offset]
	print("node=",node," start_char =", start_char, " mid_char =", mid_char, " start=", start, " offset=", offset)

	return 0


def suffix_array_to_suffix_tree(sa, lcp, text):
	"""
		Use tree structure where tree is dict
			tree = { 0: {'A':1, '$':2 }}
			edge_array = [[None, None] for _ in range(len())]
	"""

	lcp_prev = 0
	cur_node = 0

	for i in range(len(text) - 1):
		suffix = sa[i]
		print("suffix=", suffix, " cur_node=", cur_node, " lcp_prev=", lcp_prev," tree=",tree)

		while string_depth_array[cur_node] > lcp_prev:
			print('> set cur_node to parent_array[cur_node]')
			cur_node = parent_array[cur_node]
			print('> cur_node=', cur_node)

		if string_depth_array[cur_node] == lcp_prev:
			print('  >> string_depth_array[cur_node] == lcp_prev', lcp_prev)
			print('    >> create new leaf')
			cur_node = create_new_leaf(cur_node, text, suffix)
		else:
			print('>>> ')
			edge_start = sa[i-1] + string_depth_array[cur_node]
			offset = lcp_prev - string_depth_array[cur_node]
			mid_node = break_edge(cur_node, text, edge_start, offset)
			# cur_node = create_new_leaf

		print("children_array", children_array)
		print("parent_array",parent_array)
		print("string_depth_array",string_depth_array)
		print("edge_start_array",edge_start_array)
		print("edge_end_array",edge_end_array)
		print("TREE=", tree)

		print("\n")

		if i < len(text)-1:
			lcp_prev = lcp[i]
	
	print("FINAL TREE=", tree)
	return tree


if __name__ == '__main__':
	# Adjusted my tree printing function from recursive to 
	# iterative to pass assignment
	text = sys.stdin.readline().strip()
	sa = list(map(int, sys.stdin.readline().strip().split()))
	lcp = list(map(int, sys.stdin.readline().strip().split()))

	# Declare global variables
	tree = {0:{}} # root
	# children_array = [{}] # default for root node
	# parent_array = [None]
	# string_depth_array = [0]
	# edge_start_array = [-1]
	# edge_end_array = [-1]
	children_array = [{} for _ in range(len(text)+1)]
	parent_array = [None for _ in range(len(text)+1)]
	string_depth_array = [0 for _ in range(len(text)+1)]
	edge_start_array = [-1 for _ in range(len(text)+1)]
	edge_end_array = [-1 for _ in range(len(text)+1)]

	print(text)

	# Build the suffix tree and get a mapping from 
	# suffix tree node ID to the list of outgoing Edges.
	tree = suffix_array_to_suffix_tree(sa, lcp, text)

	# results = []
	# stack = [(0, 0)]
	# result_edges = []

	# while len(stack) > 0:
	# 	(node, edge_index) = stack[-1]
	# 	stack.pop()
	# 	if not node in tree:
	# 		continue
	# 	edges = tree[node]
	# 	if edge_index + 1 < len(edges):
	# 		stack.append((node, edge_index + 1))
	# 	print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
	# 	stack.append((edges[edge_index][0], 0))
