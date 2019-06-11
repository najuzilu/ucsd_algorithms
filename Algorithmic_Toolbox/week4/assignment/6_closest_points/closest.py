#Uses python3
import sys
import math

def merge(left, right):
	merged_array = []
	while left != [] and right != []:
		left_element = left[0]
		right_element = right[0]
		if left_element[0] <= right_element[0]:
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

def sort_array(array, left, right, other):
	if right - left <= 1:
		return [(array[left:right][0], other[left:right][0])]
	ave = (left + right) // 2
	left_array = sort_array(array, left, ave, other)
	right_array = sort_array(array, ave, right, other)
	sorted_array = merge(left_array, right_array)
	return sorted_array

def closest_split_pair(p_x, d):
	pass

def minimum_distance(p_x):
	'''
		1. math.sqrt() only at the end
		2. check only 5 values
	'''
	# checkout: https://www.youtube.com/watch?v=3pUOv_ocJyA 
	# print('p_x={}, p_y={}'.format(p_x, p_y))
	print(p_x)
	delta, old_delta = 0.0, math.inf
	if len(p_x) <= 3:
		p, q = (), ()
		for i in range(len(p_x) - 1):
			q_x, q_y = p_x[i][0], p_x[i][1] # left half
			r_x, r_y = p_x[i+1][0], p_x[i+1][1] # right half
			delta = (q_x - r_x)**2 + (q_y - r_y)**2
			if delta < old_delta:
				old_delta = delta
				p, q = p_x[i], p_x[i+1]
		return p, q
	left, right = 0, len(p_x)
	mid = (right - left) // 2
	left, right = p_x[left:mid], p_x[mid:right]
	p1, q1 = minimum_distance(left)
	p2, q2 = minimum_distance(right)
	d1 = (p1[0] - q1[0])**2 + (p1[1] - q1[1])**2
	d2 = (p2[0] - q2[0])**2 + (p2[1] - q2[1])**2
	delta = min(d1, d2)
	print('min delta=', delta)
	'''
	# # step 3: (p3, q3) = closestSplitPair(px ,py)
	# # step 4: return best of (p1,q1) (p2,q2) (p3,q3)
	'''

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	print('x={}, y={}'.format(x,y))
	p_x = sort_array(x, 0, len(x), y)
	print(minimum_distance(p_x))
	# print("{0:.9f}".format(minimum_distance(x, y, 0, len(x))))