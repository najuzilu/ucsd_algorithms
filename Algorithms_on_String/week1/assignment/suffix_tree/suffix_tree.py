# python3
import sys
import collections

def sort_characters(s):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	order = [None for _ in range(len(s))]
	count = [0 for _ in range(len(alphabet))]
	
	dict_map = {}
	for i in range(len(s)):
		if s[i] == '$':
			idx = ord('$') - ord('$')
		else:
			idx = ord(s[i]) - ord('A') + 1

		if s[i] not in dict_map.keys():
			dict_map[s[i]] = idx
		count[idx] += 1
	for j in range(1, len(alphabet)):
		count[j] = count[j] + count[j - 1]
	for i in range(len(s) - 1, -1, -1):
		c = s[i]
		count[dict_map[c]] = count[dict_map[c]] - 1
		order[count[dict_map[c]]] = i
	return order

def compute_char_classes(s, order):
	class_array = [None for _ in range(len(s))]
	class_array[order[0]] = 0

	for i in range(1, len(s)):
		if s[order[i]] != s[order[i-1]]:
			class_array[order[i]] = class_array[order[i-1]] + 1
		else:
			class_array[order[i]] = class_array[order[i-1]]
	return class_array

def sort_doubled(s, L, order, class_array):
	count = [0 for _ in range(len(s))]
	newOrder = [None for _ in range(len(s))]

	for i in range(0, len(s)):
		count[class_array[i]] += 1

	for j in range(1, len(s)):
		count[j] = count[j] + count[j-1]
	for i in range(len(s)-1, -1, -1):
		start = (order[i] - L + len(s)) % len(s)
		cl = class_array[start]
		count[cl] -= 1
		newOrder[count[cl]] = start
	return newOrder

def update_classes(order, class_array, L):
	n = len(order)
	new_class = [None for _ in range(n)]
	new_class[order[0]] = 0

	for i in range(1, n):
		cur = order[i]
		prev = order[i-1]
		mid = (cur + L) % n
		mid_prev = (prev + L) % n

		if class_array[cur] != class_array[prev] or class_array[mid] != class_array[mid_prev]:
			new_class[cur] = new_class[prev] + 1
		else:
			new_class[cur] = new_class[prev]
	return new_class

def build_suffix_array(text):
	order = sort_characters(text)
	class_array = compute_char_classes(text, order)
	L = 1

	while L < len(text):
		order = sort_doubled(text, L, order, class_array)
		class_array = update_classes(order, class_array, L)
		L *= 2

	return order

def lcp_of_suffixes(s, i, j, equal):
	lcp = max(0, equal)
	while (i + lcp < len(s)) and (j + lcp < len(s)):
		if s[i +lcp] == s[j + lcp]:
			lcp += 1
		else:
			break
	return lcp

def invert_suffix_array(order):
	pos = [None for _ in range(len(order))]
	for i in range(0, len(pos)):
		pos[order[i]] = i
	return pos

def compute_lcp_array(s, order):
	lcp_array = [None for _ in range(len(s) - 1)]
	lcp = 0

	pos_in_order = invert_suffix_array(order)
	suffix = order[0] # could be order[1]

	for i in range(len(s)):
		order_idx = pos_in_order[suffix]
		if order_idx == len(s) - 1:
			lcp = 0
			suffix = (suffix + 1) % len(s)
			continue
		next_suffix = order[order_idx + 1]
		lcp = lcp_of_suffixes(s, suffix, next_suffix, lcp-1)
		lcp_array[order_idx] = lcp
		suffix = (suffix + 1) % len(s)
	return lcp_array

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

	for i in range(len(text)):
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

def build_suffix_tree(text):
	result = []
	sa = build_suffix_array(text)
	lcp = compute_lcp_array(text, sa)
	tree = suffix_array_to_suffix_tree(sa, lcp, text)

	stack = [tree]

	while len(stack) > 0:
		node = stack[-1]
		stack.pop()
		if node.edge_start != -1 and node.edge_end != -1:
			result.append(text[node.edge_start: node.edge_end])
		for j in range(len(node.children)-1, -1, -1): # in reverse order
			stack.append(list(node.children.values())[j])
	return result

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	result = build_suffix_tree(text)
	print("\n".join(result))