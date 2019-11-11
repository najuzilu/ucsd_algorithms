# python3
import sys

def sort_characters(s):
	"""
		Sort single characters
	"""
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	order = [None for _ in range(len(s))]
	count = [0 for _ in range(len(alphabet))]
	
	dict_map = {} # keeps track of mappings from letter to unique value

	# First iteration {s[i] appears count[dict_map[s[i]]] times in text}
	for i in range(len(s)):
		if s[i] == '$':
			idx = ord('$') - ord('$')
		else:
			idx = ord(s[i]) - ord('A') + 1

		if s[i] not in dict_map.keys():
			dict_map[s[i]] = idx
		count[idx] += 1

	for j in range(1, len(alphabet)): # length of alphabet
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

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	print(" ".join(map(str, build_suffix_array(text))))
