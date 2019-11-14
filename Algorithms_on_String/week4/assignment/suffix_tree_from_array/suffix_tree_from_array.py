# python3
import sys
import collections

class suffix_tree_node(object):
	def __init__(self, children, parent, string_depth, edge_start, edge_end):
		self.children = collections.OrderedDict(children)
		self.parent = parent
		self.string_depth = string_depth
		self.edge_start = edge_start
		self.edge_end = edge_end

def create_new_leaf(node, s, suffix):
	leaf = suffix_tree_node({}, node, len(s) - suffix, suffix + node.string_depth, len(s))
	node.children[s[leaf.edge_start]] = leaf
	return leaf

def break_edge(node, s, start, offset, suffix):
	start_char = s[start]
	mid_char = s[start + offset]

	# Node that is split
	mid_node = suffix_tree_node({}, node, node.string_depth + offset, start, start + offset)

	# Add left over from split to split node => add node '$' to node 'A'
	mid_node.children[mid_char] = node.children[start_char] 
	
	# Modifies leaf from split which is correct
	node.children[start_char].parent = mid_node
	node.children[start_char].edge_start += offset
	node.children[start_char] = mid_node
	return mid_node

def suffix_array_to_suffix_tree(sa, lcp, text):
	root = suffix_tree_node({}, None, 0, -1, -1)
	lcp_prev = 0
	cur_node = root

	for i in range(len(text)): # -2 for sample8
		suffix = sa[i]

		while cur_node.string_depth > lcp_prev:
			cur_node = cur_node.parent

		if cur_node.string_depth == lcp_prev:
			cur_node = create_new_leaf(cur_node, text, suffix)
		else:
			edge_start = sa[i-1] + cur_node.string_depth
			offset = lcp_prev - cur_node.string_depth
			mid_node = break_edge(cur_node, text, edge_start, offset, suffix)
			cur_node = create_new_leaf(mid_node, text, suffix)

		if i < len(text)-1:
			lcp_prev = lcp[i]
	return root

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

	stack = [tree]
	result_edges = []

	while len(stack) > 0:
		node = stack[-1]
		stack.pop()
		if node.edge_start != -1 and node.edge_end != -1:
			print(node.edge_start, node.edge_end)
			result_edges.append((node.edge_start, node.edge_end))
		for j in range(len(node.children)-1, -1, -1): # in reverse order
			stack.append(list(node.children.values())[j])