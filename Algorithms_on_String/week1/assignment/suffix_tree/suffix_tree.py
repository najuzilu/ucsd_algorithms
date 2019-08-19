# python3
import sys

def suffix_tree(text):
	tree = {} 
	iter_ = 0 # to keep track # of nodes
	
	inf_list = [ [None, None] for _ in range(len(text) * 2)] # list to store [start_idx, length] for each node
	inf_list[iter_] = [0, len(text)] # 1st node info > add all text
	tree[iter_] = {text[0] : iter_ + 1} # 1st node in tree
	iter_ += 1
	length_cst = len(text) # length of text constant

	for i in range(1, len(text)):
		cur = 0 # set current node to root node for each iter of text
		count = 0 # count # of same letters
		if text[i] in tree[cur].keys(): # if first letter in root
			cur = tree[cur][text[i]] # find node after root
			cur_info = inf_list[cur - 1] # subtract one because inf_list starts index 0
			start_idx, length = cur_info[0], cur_info[1]
			j = i
			while text[j] == text[start_idx]:
				count += 1
				start_idx += 1
				j += 1
				length -= 1
				if length == 0:
					if text[j] in tree[cur].keys():
						cur = tree[cur][text[j]] # find node after root
						cur_info = inf_list[cur - 1] # subtract one because inf_list starts index 0
						start_idx, length = cur_info[0], cur_info[1]
						count -= 1
			if cur in tree.keys():
				if count < inf_list[cur - 1][1]:
					tree[iter_ + 1] = tree[cur]
					inf_list[iter_] = [inf_list[cur - 1][0] + count, length]
					tree[cur] = {text[start_idx] : iter_ + 1}
					inf_list[cur - 1][1] = count
					iter_ += 1
				# update tree with new node
				tree[cur][text[j]] = iter_ + 1
				inf_list[iter_] = [j, length_cst - j]
				iter_ += 1
			else:
				# update inf_list with the new node with parent node information
				x = inf_list[cur - 1][0] + count
				inf_list[iter_] = [x, length_cst - x]
				# update inf_list parent node
				inf_list[cur - 1][1] = count
				# create the new node from the parent node info
				tree[cur] = {text[start_idx] : iter_ + 1}
				iter_ += 1

				# update inf_list with the new branch
				inf_list[iter_] = [j, length_cst - j]
				# create the new node from the parent node info
				tree[cur][text[j]] = iter_ + 1
				iter_ += 1
		else: # if first letter not in root
			tree[cur][text[i]] = iter_ + 1
			inf_list[iter_] = [i, len(text) - i]
			iter_ += 1
		# print('i =', i)
		# print('tree =', tree)
		# print('inf_list =', inf_list)
		# print('\n')
	return tree, inf_list

def build_suffix_tree(text):
	"""
	Build a suffix tree of the string text and return a list
	with all of the labels of its edges (the corresponding 
	substrings of the text) in any order.
	"""
	results = []
	tree, suffix_tree_inf = suffix_tree(text)

	for node in tree:
		for c in tree[node]:
			text_range = suffix_tree_inf[tree[node][c] - 1]
			start_index = text_range[0]
			text_len = text_range[1]
			results.append(text[start_index: start_index + text_len])
	return results

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	result = build_suffix_tree(text)
	print("\n".join(result))