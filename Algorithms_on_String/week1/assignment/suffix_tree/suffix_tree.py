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

def match_from_root(tree, node_idx, string, main_text):
	for key, value in tree[node_idx].items():
		if string == main_text[value[0]]:
			return key
	return False

tree = {0: {1:[0, 1]}, 1: {3:[1, 7], 4:[3, 5]}}
main_text = 'ATAAATG$'

def find_node_match(tree, node_idx, element, el_iter, main_text):
	dummy_key = False
	for key, value in tree[node_idx].items():
		print('Looping through node: {}-{}'.format(key, value))
		node_text_iter = value[0]
		node_text_len = value[1]
		if el_iter < len(element):
			 while element[el_iter] == main_text[main_text_iter]:
		elif el_iter == len(element):

		while el_iter <= len(element) and element[el_iter] == main_text[main_text_iter]:


			
	return False


def build_tree(patterns, main_text):
	tree = {}
	iter_ = 1 # keep track of nodes
	new_node_idx = 0 # keep track of children
	count = 0

	for i in range(len(patterns) - 4):
		print('Looping through pattern: ', patterns[i])
		element = patterns[i]
		node_idx = 0 # root node
		if i == 0:
			tree[node_idx] = {iter_: [i, len(element)]}
			iter_ += 1
		else:
			while element:
				string = element[0]
				new_node_idx = match_from_root(tree, node_idx, string, main_text)
				if not new_node_idx:
					print('String {} does not exist...'.format(string))
					"""
						if node_idx has children or does not have children >> do different things?
					"""
					tree[node_idx][iter_] = [i, len(element)]
					iter_ += 1
					break
				else:
					print('String {} exists and matched node_idx = {}'.format(string, new_node_idx))
					count += 1

				element = element[1:]
		print('tree =',tree)
		print('\n')
	return tree


def build_tree_(patterns, main_text):
	tree = {}
	iter_ = 1 # keep track of nodes
	new_node_idx = 0 # keep track of new node
	count = 0

	for i in range(len(patterns) - 4): # TESTING # 3 // -4
		element = patterns[i]
		node_idx = 0 # current node index
		count = 0 # to count how many same strings
		print('Looping through pattern: ', element)
		if i == 0: # if first element
			tree[node_idx] = {iter_: [i, len(element)]}
			iter_ += 1
		else:

			for j in range(len(element)):
				string = element[j]
				print('j =', j)
				if j == 0: # find if first string of element is in one of the children from the root
					print('   Finding if first string matches with any nodes from root...')
					new_node_idx = match_from_root(tree, node_idx, string, main_text)
					if not new_node_idx:
						print('   First string did not match with any nodes')
						tree[node_idx][iter_] = [i, len(element)]
						iter_ += 1
						break # first string does not match with any of the children from the root node so break loop of element and continue to next pattern
					else: 
						print('   First string matched with node w/ node_idx ', new_node_idx)
						count += 1

				else:
					start_idx, length = tree[node_idx][new_node_idx][0], tree[node_idx][new_node_idx][1]
					if j > length:
						print('****Element={} has greater length than node_word={}>>> Go to next nodes?'.format(element, main_text[start_idx:length]))
					else:
						if j == length:
							node_idx = new_node_idx
							new_node_idx = match_from_root(tree, new_node_idx, string, main_text)

						if string == main_text[start_idx + j]:
							count += 1
						else:
							print('   BREAK NODE>>> new_node_idx=',new_node_idx)
							if new_node_idx in tree.keys():
								# if node already exists, split
								print('   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
								print('   MATCH=',match_from_root(tree, new_node_idx, string, main_text))
								print('   node_idx={}, new_node_idx={}, iter_={}, count={}, j={}'.format(node_idx, new_node_idx, iter_, count, j))
								
								# tree[iter_] = tree[new_node_idx]
								# tree[node_idx][new_node_idx][1] = count
								# tree[new_node_idx] = {iter_: [j, len(element) - j - count]}
								# iter_ += 1
								# tree[new_node_idx][iter_] = [i + j, len(element) - j] ### ?????? not entirely sure about i + j
								break
							else:
								# node does not exist so create one
								print('new_node_idx={}, iter_={}, count={}, start_idx={}'.format(new_node_idx, iter_, count, start_idx))

								tree[new_node_idx] = {iter_: [tree[node_idx][new_node_idx][0] + count, tree[node_idx][new_node_idx][1] - count]} # creates new branch with first node being filled by the main node being split
								iter_ += 1
								print('new_node_idx={}, iter_={}, count={}, start_idx={}'.format(new_node_idx, iter_, count, start_idx))
								tree[new_node_idx][iter_] = [j + i, len(element) - j] # create new node on the same branch as above
								tree[node_idx][new_node_idx][1] = j
								iter_ += 1
								break
		print(tree)
		print('\n')	
	return tree


def build_suffix_tree(text):
	"""
	Build a suffix tree of the string text and return a list
	with all of the labels of its edges (the corresponding 
	substrings of the text) in any order.
	"""
	# result = []
	# print('TEXT = ', text)
	# suffixes = suffix_array(text)
	# print('SUFFIXIES: ', suffixes, '\n')
	
	# # Build tree from scratch
	# # patterns =  ['AAAATG$', 'AAATG$', 'AATG$'] 
	# # build_tree(patterns, patterns[0])

	# build_tree(suffixes, text)
		

	

	return result


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	result = build_suffix_tree(text)
	print("\n".join(result))