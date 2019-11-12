# python3
import sys

def sort_characters(s):
	"""
		Sort single characters
	"""
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	# alphabet = 'abcdefghijklmnopqrstuvwxyz'
	order = [None for _ in range(len(s))]
	count = [0 for _ in range(len(alphabet))]
	
	dict_map = {}

	for i in range(len(s)):
		if s[i] == '$':
			idx = ord('$') - ord('$')
		else:
			idx = ord(s[i]) - ord('A') + 1
			# idx = ord(s[i]) - ord('a') + 1

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
	"""
	Build suffix array of the string text and
	return a list result of the same length as the text
	such that the value result[i] is the index (0-based)
	in text where the i-th lexicographically smallest
	suffix of text starts.
	"""
	order = sort_characters(text)
	class_array = compute_char_classes(text, order)
	L = 1

	while L < len(text):
		order = sort_doubled(text, L, order, class_array)
		class_array = update_classes(order, class_array, L)
		L *= 2
	return order

# def lcp_of_suffixes(s, i, j, equal):
# 	lcp = max(0, equal)
# 	while (i + lcp < len(s)) and (j + lcp < len(s)):
# 		if s[i +lcp] == s[j + lcp]:
# 			lcp += 1
# 		else:
# 			break
# 	return lcp

# def invert_suffix_array(order):
# 	pos = [None for _ in range(len(order))]
# 	for i in range(0, len(pos)):
# 		pos[order[i]] = i
# 	return pos

# def compute_lcp_array(s, order):
# 	lcp_array = [None for _ in range(len(s) - 1)] # could be len(s)
# 	lcp = 0

# 	pos_in_order = invert_suffix_array(order)
# 	suffix = order[0] # could be order[1]

# 	for i in range(len(s)):
# 		order_idx = pos_in_order[suffix]
# 		if order_idx == len(s) - 1:
# 			lcp = 0
# 			suffix = (suffix + 1) % len(s)
# 			continue
# 		next_suffix = order[order_idx + 1]
# 		lcp = lcp_of_suffixes(s, suffix, next_suffix, lcp-1)
# 		lcp_array[order_idx] = lcp
# 		suffix = (suffix + 1) % len(s)
# 	return lcp_array

def first_occurance(string):
	dict_ = {}
	string = sorted(string)
	previousStr = string[0]
	dict_[string[0]] = 0
	for i in range(1, len(string)):
		if string[i] != previousStr:
			dict_[string[i]] = i
		previousStr = string[i]
	return dict_

def preprocess_bwt(bwt):
	occ_counts_before = []
	dictRow = {k: 0 for k in set(sorted(bwt))}

	startsDict = first_occurance(bwt)
	for char in bwt:
		occ_counts_before.append(dictRow.copy())
		dictRow[char] += 1
	occ_counts_before.append(dictRow.copy())
	return startsDict, occ_counts_before

def count_occurrences(pattern, bwt, starts, occ_counts_before, order, text):
	top = 0
	bottom = len(bwt) - 1

	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]

			if symbol in occ_counts_before[top].keys():
				top = starts[symbol] + occ_counts_before[top][symbol]
				bottom = starts[symbol] + occ_counts_before[bottom + 1][symbol] - 1
			else:
				return (0, 0)
		else:
			return (bottom, top)
	return (0, 0)

def find_occurrences(text, patterns):
	occs = set()

	text = text + '$'

	# Construct suffix array
	suffix_array = build_suffix_array(text)
	
	# Construct BWT string
	bwt = ''
	for i in range(len(suffix_array)):
		bwt += text[suffix_array[i]-1]

	# Use BWT Pattern Matching Algo
	starts, occ_counts_before = preprocess_bwt(bwt)

	occurrence_counts = []
	for pattern in patterns:
		bottom, top = count_occurrences(pattern, bwt, starts, occ_counts_before, suffix_array, text)
		if top == bottom:
			if text[suffix_array[top]] == pattern[0]:
				occs.add(suffix_array[top])
		else:
			for i in range(top, bottom + 1):
				occs.add(suffix_array[i])
	return occs

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	pattern_count = int(sys.stdin.readline().strip())
	patterns = sys.stdin.readline().strip().split()
	occs = find_occurrences(text, patterns)
	print(" ".join(map(str, occs)))