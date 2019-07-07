#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

def build_new_branch(tree, j, element, count):
	for i in range(j, len(element)):
		tree[count] = {element[i] : count + 1}
		count += 1
	return tree, count

def build_trie(patterns):
	tree = dict()
	iter_ = 0
	for i in range(len(patterns)):
		element = patterns[i]
		current_node = 0
		if i == 0:
			for j in range(len(element)):
				string = element[j]
				tree[iter_] = {string: iter_ + 1}
				iter_ += 1
		else:
			for j in range(len(element)):
				string = element[j]
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

if __name__ == '__main__':
	patterns = sys.stdin.read().split()[1:]
	tree = build_trie(patterns)
	for node in tree:
		for c in tree[node]:
			print("{}->{}:{}".format(node, tree[node][c], c))
