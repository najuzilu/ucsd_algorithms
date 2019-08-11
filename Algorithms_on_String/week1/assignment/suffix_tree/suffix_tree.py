# python3
import sys

def build_suffix_tree(text):
	"""
	Build a suffix tree of the string text and return a list
	with all of the labels of its edges (the corresponding 
	substrings of the text) in any order.
	"""
	print('Looping through text =', text)
	tree = {} 
	iter_ = 0 # to keep track # of nodes
	
	inf_list = [ [None, None] for _ in range(len(text) * 2)] # list to store [start_idx, length] for each node
	inf_list[iter_] = [0, len(text)] # 1st node info > add all text
	tree[iter_] = {text[0] : iter_ + 1} # 1st node in tree
	iter_ += 1
	length_cst = len(text) # length of text constant

	for i in range(1, len(text)): # - 4
		print('LOOPING THROUGH ', text[i:])
		cur = 0 # set current node to root node for each iter of text
		count = 0 # count # of same letters
		if text[i] in tree[cur].keys(): # if first letter in root
			cur_next = tree[cur][text[i]] # find node after root
			cur_next_info = inf_list[cur_next - 1] # subtract one because inf_list starts index 0
			start_idx, length = cur_next_info[0], cur_next_info[1]
			j = i
			while text[j] == text[start_idx]:
				print('i={}, j={}, start_idx={}, text[i]={}, text[j]={}, text[start_idx]={},length={}'.format(i,j,start_idx,text[i], text[j], text[start_idx], length))
				count += 1
				start_idx += 1
				j += 1
				if length - 1 == 0:
					cur = tree[cur][text[i]] # find node after root
					cur_next_info = inf_list[cur - 1] # subtract one because inf_list starts index 0
					start_idx, length = cur_next_info[0], cur_next_info[1]
					# j += 1
				
					print('update new node: ', cur)
					print('>>i={}, j={}, start_idx={}, text[i]={}, text[j]={}, text[start_idx]={},length={}'.format(i,j,start_idx,text[i], text[j], text[start_idx], length))

			print('iter_={}, count={}, j={}'.format(iter_,count, j))
			# update inf_list with the new node with parent node information
			inf_list[iter_] = [inf_list[tree[cur][text[i]] - 1][0] + count, inf_list[tree[cur][text[i]] - 1][1] - count]
			# update inf_list parent node
			inf_list[tree[cur][text[i]] - 1][1] = count
			# create the new node from the parent node info
			tree[tree[cur][text[i]]] = {text[inf_list[tree[cur][text[i]] - 1][0] + count] : iter_ + 1}
			iter_ += 1

			# update inf_list with the new branch
			inf_list[iter_] = [j, length_cst - j]
			# create the new node from the parent node info
			tree[tree[cur][text[i]]][text[j]] = iter_ + 1
			iter_ += 1

		else: # if first letter not in root
			tree[cur][text[i]] = iter_ + 1
			inf_list[iter_] = [i, len(text) - i]
			iter_ += 1

		print(tree)
		print(inf_list)
		print('\n')
	print('\n')
	print(tree)
	print(inf_list)

	return ''


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	result = build_suffix_tree(text)
	print("\n".join(result))