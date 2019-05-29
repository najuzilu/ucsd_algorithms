# Uses python3
import sys

def count_if_majority(a, left, right, element):
	count = 0
	for i in range(right - left):
		if a[left + i] == element:
			count += 1
	if count / (right- left) > 0.5:
		return count
	return -1

def get_majority_element_test(a, left, right):
	'''
		This approach is still in testing:
		>> test case 9 should be 1 but is instead 0
	'''
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
	mid_point = int((right - left)/2 + left)
	# Get left and right elements
	left_el = get_majority_element(a, left, mid_point)
	right_el = get_majority_element(a, mid_point + 1, right)
	if left_el == -1 and right_el == -1:
		# if both are -1
		return -1
	elif left_el != -1 and right_el == -1:
		# if left_el
		if count_if_majority(a, left, right, left_el) > 1:
			return left_el
		else:
			return -1
	elif left_el == -1 and right_el != -1:
		# if right_el
		if count_if_majority(a, left, right, right_el) > 1:
			return right_el
		else:
			return -1
	else:
		# if both, count both and determine
		left_count = count_if_majority(a, left, right, left_el)
		right_count = count_if_majority(a, left, right, right_el)
		if left_count >= right_count:
			return left_el
		else:
			return right_el

def get_majority_element(a, left, right):
	'''
		This approach does not use divide and conquer
		Naive implementation
	'''
	dict_row = {}
	for each in a:
		if each not in dict_row.keys():
			dict_row[each] = 1
		else:
			dict_row[each] += 1
	key_max = max(dict_row.keys(), key=(lambda k: dict_row[k]))
	if dict_row[key_max] / len(a) > 0.5:
		return dict_row[key_max]
	else:
		return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)
