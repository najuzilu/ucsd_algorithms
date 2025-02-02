# python3
import sys
import collections

def sort_characters(s):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#'
	order = [None for _ in range(len(s))]
	count = [0 for _ in range(len(alphabet))]
	
	dict_map = {}
	for i in range(len(s)):
		if s[i] == '$':
			idx = ord('$') - ord('$')
		elif s[i] == '#':
			idx = ord('$') - ord('$') + 1
		else:
			idx = ord(s[i]) - ord('A') + 2

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
		self.mark = False

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





"""
Then you will find that the leaves whose path start from TEXT1 always contain # sign (type L leaf). 
And those don't contain # sign and ending with $ sign are leaves whose path starts from TEXT2 (type R leaf).

The next step is to check every type L leaf. A candidate answer would be the path + the first letter of type 
L leaf (except for the case that type L leaf starts with #), because we are not sure whether the path is shared 
with some type R leaves, by adding the first letter of the current type L leaf we can make sure the substring is 
not shared by any type R leaf (an exception in next paragraph). Then you just have to select the shortest candidate.

However, note that if a non-leaf node has type L leaves only, it means that the candidate answer would be only the 
path ending at the current non-leaf node instead of the path + the first letter of the left leaf. In this case, we 
are sure that the path is shared by type L leaves only, thus there is no need to add an extra letter.
"""


# def has_path(node, end_node, string):
# 	"""
# 		If node in path, it append to paths list
# 	"""
# 	global path

# 	if node.edge_start != -1 and node.edge_end != -1:
# 		path += string[node.edge_start:node.edge_end]
# 		# if node.children == {}:
# 		# 	path += string[node.edge_start]
# 		# else:
# 		# 	path += string[node.edge_start:node.edge_end]

# 	if (node == end_node):
# 		return True

# 	for child in node.children.values():
# 		if has_path(child, end_node, string):
# 			return True

# 	path = path[:-1]
# 	return False

# def path_to(node, end_node, string):
# 	"""
# 		Calls has_path method
# 	"""
# 	global path
# 	path = ''
# 	if (has_path(node, end_node, string)):
# 		return path

# def explore(node, string):
# 	"""
# 		Find all nodes that are part of text 1 and set mark to True
# 	"""
# 	for child in node.children.values():
# 		explore(child, string)

# 	if node.children == {} and '#' in string[node.edge_start: node.edge_end]: #and not string[node.edge_start: node.edge_end].startswith('#')
# 		node.mark = True
# 		L_nodes.append(node)
# 	else:
# 		for child in node.children.values():
# 			if child.mark == True:
# 				node.mark = True
# 				break

def print_array(ints, len):
	""" TESTING """
	for i in ints[0: len]:
		print(i, " ", end = "")
	print()

def append_path(ints, len):
	path = ''
	for each in ints:
		if each.startswith('#'):
			return ''
		elif '#' in each:
			path += each[0]
		else:
			path += each
	return path

def explore(node, string):
	"""
		Mark all nodes that have leaf children as True
	"""
	if '#' in string[node.edge_start: node.edge_end] and len(node.children) == 0:
		node.mark = True
	for child in node.children.values():
		explore(child, string)

def explore2(node, string):
	print(string[node.edge_start:node.edge_end], ' -> ',node.mark)
	for child in node.children.values():
		explore2(child, string)

def print_paths_rec(node, path, string, pathLen):
	global result

	if (len(path) > pathLen):
		path[pathLen] = string[node.edge_start: node.edge_end]
	else:
		path.append(string[node.edge_start: node.edge_end])
	pathLen += 1

	### checks if children are leaf L nodes
	node_children = list(node.children.values())
	array = [False for _ in range(len(node_children))]
	for i in range(len(node_children)):
		array[i] = node_children[i].mark
	if False not in array and len(array) > 0:
		n = string[node.edge_start: node.edge_end]
		if n not in string[string.find('#'):]:
			result.append(n)

	if len(node.children) == 0:
		if '#' in string[node.edge_start: node.edge_end]:
			# print_array(path, pathLen)
			concat_path = append_path(path[:pathLen], pathLen)
			if concat_path != '': result.append(concat_path)
	else:
		for child in node.children.values():
			print_paths_rec(child, path, string, pathLen)


def solve (p, q):
	# Construct suffix tree of TEXT1#TEXT2$
	text = p + '#' + q + '$'
	sa = build_suffix_array(text)
	lcp = compute_lcp_array(text, sa)
	tree = suffix_array_to_suffix_tree(sa, lcp, text)

	explore(tree, text)

	global result
	path, result = [], []
	print_paths_rec(tree, path, text, 0)

	# print("\n")
	# for each in result:
	# 	print(each)

	return min(result, key=len)

p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)
sys.stdout.write (ans + '\n')