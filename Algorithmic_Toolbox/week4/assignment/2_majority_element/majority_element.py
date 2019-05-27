# Uses python3
import sys

def get_majority_element(a, left, right):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
	mid_point = int((right - left)/2 + left)
	# Get left and right elements
	left_el = get_majority_element(a, left, mid_point)
	right_el = get_majority_element(a, mid_point + 1, right)
	print(left_el, right_el)
	return
	
if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	print(get_majority_element(a, 0, n))
	# if get_majority_element(a, 0, n) != -1:
	# 	print(1)
	# else:
	# 	print(0)
