# python3
import sys

def build_suffix_tree(text = 'CAGTCAGG'):
	"""
	Build a suffix tree of the string text and return a list
	with all of the labels of its edges (the corresponding 
	substrings of the text) in any order.
	"""
	tree = {}
	iter_ = 0
	
	text += '$'
	inf_list = [ [None, None] for _ in range(len(text) * 2)]
	inf_list[iter_] = [0, len(text)]
	tree[iter_] = {text[0] : iter_ + 1}
	iter_ += 1
	length_cst = len(text)

	for i in range(1, len(text)): # remove - 1
		cur = 0
		count = 0
		# print('looping through s:', text[i:], ' TREE =', tree)
		if text[i] in tree[cur].keys():
			# find which branch from root it's
			start_idx, length = inf_list[tree[cur][text[i]] - 1][0], inf_list[tree[cur][text[i]] - 1][1]
			# print('>> ', text[i], tree[cur][text[i]])
			# print('>> start_idx={}, length={}'.format(start_idx, length))
			j = i
			while (j < length_cst) and (text[j] == text[start_idx]):
				# print(text[j], ' ==', text[start_idx], '; j=', j, ' cur=',cur, ' length=', length)
				count += 1
				j += 1
				start_idx += 1
			if j == length_cst - 1:
				# fully identical to cur so update cur
				# print('all letters are identical to the node from root so try to find if there are any children to __cur__ node')
				# update inf_list with the new branch
				inf_list[iter_] = [j, length_cst - j]
				# create the new node from the parent node info
				tree[tree[cur][text[i]]][text[j]] = iter_ + 1
				iter_ += 1
			else:
				# print('j=', j, ' iter_=', iter_, 'count=', count)
				# print(inf_list[tree[cur][text[i]] - 1][0], inf_list[tree[cur][text[i]] - 1][1])

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

		else:
			tree[cur][text[i]] = iter_ + 1
			inf_list[iter_] = [i, len(text) - i]
			iter_ += 1

	print(tree)
	print(inf_list)
	print('\n')
	return ''


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	result = build_suffix_tree() # text as input
	print("\n".join(result))