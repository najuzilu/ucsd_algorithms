# python3
import sys

def suffix_array(text):
	array = []
	while len(text):
		array.append(text)
		text = list(text)
		text.pop(0)
		text = ''.join(text)
	return array

def build_tree(patterns, main_text):
	tree = {}
	iter_ = 0 # keep track of nodes
	dummy = False # to break out of outer loop after breaking inner loop

	for i in range(len(patterns) - 5): ### TESTING FILE 3
		element = patterns[i]
		print('i = {}, Adding pattern `{}` in tree {}'.format(i, element, tree))
		if i == 0:
			tree[iter_] = {iter_ + 1: [i, len(element)]}
			iter_ += 1
		else:
			node_idx = 0
			for j in range(len(element)):
				string = element[j]
				for k, v in tree[node_idx].items():
					text = main_text[v[0]: v[-1]]
					print('Element={}; text from tree is={}'.format(element, text))
					if string != text[j]:
						print('String={} != {}=text[j] from tree'.format(string, text[j]))
						if node_idx == 0:
							print('>> on root node')
							iter_ += 1
							tree[node_idx][iter_] = [i, len(element)]
							dummy = True
							break
						else:
							print('>> not on root... node_idx={}, j={}, k={}, v={}, iter_={}, TREE={}'.format(node_idx,j, k, v, iter_, tree))
							# tree[node_idx] = {iter_ + 1: [tree[node_idx][0], len]}
							# tree[k] = {iter_ + 1: []}
							# tree[k] = {iter_ + 1: [j, tree[node_idx - 1][node_idx][1]]} # append new node copied
							# iter_ += 1
							# print('>>>> node_idx={}, iter_={}, TREE={}'.format(node_idx, iter_, tree))
							# tree[node_idx][iter_ + 1] = [j, len(element)]
							# tree[node_idx - 1][node_idx][1] = j
							dummy = True
							break
					else:
						print('Strings are the same so updating node_idx to key=', k)
						node_idx = k
				if dummy == True:
					print('______BREAKING____')
					break
		print('\n')
	# tree[iter_] = {}
	print(tree)
	return tree

'''
def build_tree(patterns, main_text):
	dummy = False # dummy to break out of outer loop
	tree = {}
	iter_ = 0
	for i in range(len(patterns) - 5):
		element = patterns[i]
		print('Adding pattern `{}` in tree... {}'.format(element, tree))
		node_idx = 0
		if i == 0: # if in first iteration add to tree
			tree[iter_] = {iter_ + 1: [i, len(element)]}
			iter_ += 1
		else:
			for key,value in tree[node_idx].items(): # change to while true
				text = main_text[value[0]: value[-1]]
				for j in range(len(element)):
					string = element[j]
					print('Element is={}, text from tree is={}'.format(element, text))
					if string != text[j]:
						print('String={} != {}=text[j] from tree'.format(string, text[j]))
						if node_idx == 0:
							iter_ += 1
							tree[node_idx][iter_] = [i, len(element)]
							dummy = True
							break
						else:
							print('Strings are not the same but not current node; current_node={}; key={}; j={}; iter_={}'.format(node_idx, key, j, iter_))
							tree[key] = {iter_ + 1: [j, tree[node_idx - 1][node_idx][1]]}
							iter_ += 1
							tree[node_idx][iter_ + 1] = [j, len(element)]
							tree[node_idx - 1][node_idx][1] = j
							break
					else:
						node_idx = key
				if dummy == True:
					print('______BREAKING____')
					break
	# tree[iter_] = {}
	print(tree)
	return tree
'''

def build_suffix_tree(text):
	"""
	Build a suffix tree of the string text and return a list
	with all of the labels of its edges (the corresponding 
	substrings of the text) in any order.
	"""
	result = []
	print('TEXT = ', text)
	suffixes = suffix_array(text)
	print('SUFFIXIES: ', suffixes, '\n')
	
	# Build tree from scratch
	tree = build_tree(suffixes, text)
	# Traverse the tree and print nodes

	

	return result


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	result = build_suffix_tree(text)
	print("\n".join(result))