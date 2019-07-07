# python3
import sys

NA = -1

def build_new_branch(tree, j, element, count):
	for i in range(j, len(element)):
		tree[count] = {element[i] : count + 1}
		count += 1
	return tree, count

def build_trie(patterns):
	tree = dict()
	iter_ = 0
	for i in range(len(patterns)):
		element = patterns[i] + '$'
		current_node = 0
		if i == 0:
			for j in range(len(element)):
				string = element[j]
				tree[iter_] = {string: iter_ + 1}
				iter_ += 1
		else:
			for j in range(len(element)):
				string = element[j]
				if iter_ not in tree.keys():
					tree[iter_] = {}
				if current_node not in tree.keys():
					tree[current_node] = {}
				if string not in tree[current_node]:
					iter_ += 1
					tree[current_node][string] = iter_
					current_node = iter_
					tree, iter_ = build_new_branch(tree, j + 1, element, current_node)
					current_node += 1
					break
				else:
					current_node = tree[current_node][string]
	return tree

def trie_matching(text, i, tree):
	str_idx = i # make copy
	node_idx = 0	
	node = tree[node_idx] # root
	while True:
		if '$' in node.keys():
			return i
		elif str_idx == len(text):
			return -1
		elif text[str_idx] in node.keys():
			# find index of next child of node
			current_string = text[str_idx]
			node_idx = node[current_string]
			node = tree[node_idx]
			str_idx += 1
		else:
			return -1

def solve (text, n, patterns):
	result = []
	tree = build_trie(patterns)
	for i in range(len(text)):
		answer = trie_matching(text, i, tree)
		if answer != -1:
			result.append(answer)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
