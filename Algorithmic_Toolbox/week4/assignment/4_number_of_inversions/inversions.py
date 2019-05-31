# Uses python3
import sys

def merge(left_array, right_array):
	count = 0
	merged_array = []
	while left_array != [] and right_array != []:
		left_element = left_array[0]
		right_element = right_array[0]
		if left_element < right_element:
			merged_array.append(left_element)
			left_array.pop(0)
		else:
			merged_array.append(right_element)
			right_array.pop(0)
			count += 1
	if left_array != []:
		merged_array.extend(left_array)
	if right_array != []:
		merged_array.extend(right_array)
	return merged_array, count

def get_number_of_inversions(a, b, left, right):
	number_of_inversions = 0
	if right - left <= 1:
		return a[left:right], number_of_inversions
	ave = (left + right) // 2
	left_array, left_count = get_number_of_inversions(a, b, left, ave)
	right_array, right_count = get_number_of_inversions(a, b, ave, right)
	number_of_inversions += left_count + right_count
	merged_array, merged_count = merge(left_array, right_array)
	return merged_array, merged_count

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	b = n * [0]
	print(a)
	print(get_number_of_inversions(a, b, 0, len(a)))
