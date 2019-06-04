# Uses python3
import sys

def merge(left, right):
	merged_array = []
	while left != [] and right != []:
		left_element = left[0]
		right_element = right[0]
		if left_element <= right_element:
			merged_array.append(left_element)
			left.pop(0)
		else:
			merged_array.append(right_element)
			right.pop(0)
	if left != []:
		merged_array.extend(left)
	if right != []:
		merged_array.extend(right)
	return merged_array

def sort_array(array, left, right):
	if right - left <= 1:
		return array[left:right]
	ave = (left + right) // 2
	left_array = sort_array(array, left, ave)
	right_array = sort_array(array, ave, right)
	sorted_array = merge(left_array, right_array)
	return sorted_array

def mod_binary_search(a, x, left, right):
	if right <= left:
		return left # ?
	mid = left + ((right - left) // 2)
	if x == a[mid]:
		return mid + 1
	elif x < a[mid]:
		if right - left == 1: return mid
		right = mid
		return mod_binary_search(a, x, left, right)
	elif x > a[mid]:
		if right - left == 1: return mid + 1
		left = mid
		return mod_binary_search(a, x, left, right)

def fast_count_segments(starts, ends, points):
	cnt = [0] * len(points)	
	# step1: sort starts O(log n)
	starts_sorted = sort_array(starts, 0, len(starts))
	# step2: sort ends O(log n)
	ends_sorted = sort_array(ends, 0, len(ends))
	# step3: modified binary search for points (n log m)
	for index, point in enumerate(points):
		print(starts, ends, point, end = ' ')
		start_idx = mod_binary_search(starts_sorted, point, 0, len(starts_sorted))
		end_idx = mod_binary_search(ends_sorted, point, 0, len(ends_sorted))
		
		print('start_idx={},end_idx={}'.format(start_idx, end_idx))
		# print(starts_sorted[:start_idx], ends_sorted[:end_idx])
		if start_idx == end_idx:
			# do something else
			cnt[index] = 0
		elif start_idx > end_idx:
			cnt[index] = len(starts_sorted[:start_idx])
		else:
			cnt[index] = len(ends_sorted[:end_idx])
	return cnt

def naive_count_segments(starts, ends, points):
	cnt = [0] * len(points)
	for i in range(len(points)):
		for j in range(len(starts)):
			if starts[j] <= points[i] <= ends[j]:
				cnt[i] += 1
	return cnt

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	m = data[1]
	starts = data[2:2 * n + 2:2]
	ends   = data[3:2 * n + 2:2]
	points = data[2 * n + 2:]
	#use fast_count_segments
	# cnt = naive_count_segments(starts, ends, points)
	cnt = fast_count_segments(starts, ends, points)
	for x in cnt:
		print(x, end=' ')
