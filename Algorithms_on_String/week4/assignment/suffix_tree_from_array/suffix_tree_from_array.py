# python3
import sys

class suffix_tree_node(object):
	def __init__(self, children, parent, string_depth, edge_start, edge_end):
		self.children = children
		self.parent = parent
		self.string_depth = string_depth
		self.edge_start = edge_start
		self.edge_end = edge_end

def create_new_leaf(node, s, suffix):
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
	leaf = suffix_tree_node({}, node, len(s) - suffix, suffix + node.string_depth, len(s))
	node.children[s[leaf.edge_start]] = leaf
	print("CREATE -> " ,suffix, len(s), node.string_depth)
	return leaf

def break_edge(node, s, start, offset):
	start_char = s[start]
	mid_char = s[start + offset]
	# creates split node
	mid_node = suffix_tree_node({}, node, node.string_depth + offset, start - offset - 1 + node.string_depth, start - offset + node.string_depth) # start, start + offset - 1

	print("BREAK -> start=", start, " offset=", offset, " node.depth=", node.string_depth, " node.children[start_char].start=", node.children[start_char].edge_start, " node.children[start_char].end=", node.children[start_char].edge_end)
	
	mid_node.children[mid_char] = node.children[start_char]
	
	# modifies leaf which is correct
	node.children[start_char].parent = mid_node
	node.children[start_char].edge_start += offset
	node.children[start_char] = mid_node

	return mid_node

def suffix_array_to_suffix_tree(sa, lcp, text):
	root = suffix_tree_node({}, None, 0, -1, -1)
	lcp_prev = 0
	cur_node = root

	for i in range(len(text)):
		suffix = sa[i]

		while cur_node.string_depth > lcp_prev:
			cur_node = cur_node.parent

		if cur_node.string_depth == lcp_prev:
			print(' >')
			cur_node = create_new_leaf(cur_node, text, suffix)
		else:
			print('>>')
			edge_start = sa[i-1] + cur_node.string_depth
			offset = lcp_prev - cur_node.string_depth
			mid_node = break_edge(cur_node, text, edge_start, offset)
			cur_node = create_new_leaf(mid_node, text, suffix)
			print('mid_node -> ', mid_node.edge_start, mid_node.edge_end)

		print(suffix, " -> ",cur_node.edge_start, cur_node.edge_end)
		print("\n")

		if i < len(text)-1:
			lcp_prev = lcp[i]
	return root

def iter_tree(tree):
	for i in range(len(tree.children)-1, -1, -1):
		node = tree.children.values()[i]
		print(node.edge_start, node.edge_end)
		iter_tree(node)

if __name__ == '__main__':
	# Adjusted my tree printing function from recursive to 
	# iterative to pass assignment
	text = sys.stdin.readline().strip()
	sa = list(map(int, sys.stdin.readline().strip().split()))
	lcp = list(map(int, sys.stdin.readline().strip().split()))

	print(text)

	# Build the suffix tree and get a mapping from 
	# suffix tree node ID to the list of outgoing Edges.
	tree = suffix_array_to_suffix_tree(sa, lcp, text)

	print("\n")
	iter_tree(tree)

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
