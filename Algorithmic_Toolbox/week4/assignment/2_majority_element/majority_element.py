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

def get_majority_element(a, left, right):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
	mid_point = int((right - left)/2 + left)
	# Get left and right elements
	if len(a[left:right]) == 2:
		left_el = get_majority_element(a, left, mid_point)
		right_el = get_majority_element(a, mid_point + 1, right)
	else:
		left_el = get_majority_element(a, left, mid_point)
		right_el = get_majority_element(a, mid_point, right)
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
	
if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)
