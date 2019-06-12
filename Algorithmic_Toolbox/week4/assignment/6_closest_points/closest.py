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

def closest_split_pair(p_x, p_y, d):
	best_pair = ((),())
	mid = len(p_x) // 2
	x = p_x[mid-1][0]
	S_y = [] # sorted by y coordinate where x+/- delta
	for point in p_y:
		if (point[1] >= x - d) or (point[1] <= x + d):
			S_y.append(point)
	for i in range(0,len(S_y)-1):
		for j in range(i+1, min(len(S_y), 7)):
			diff = (S_y[i][0] - S_y[j][0])**2 + (S_y[i][1] - S_y[j][1])**2
			if diff < d:
				d = diff
				best_pair = (S_y[i], S_y[j])
	return best_pair[0], best_pair[1], d
	

def minimum_distance(p_x, p_y):
	# checkout: https://www.youtube.com/watch?v=3pUOv_ocJyA 
	delta_x, old_delta_x = 0.0, math.inf
	delta_y, old_delta_y = 0.0, math.inf
	if len(p_x) <= 3:
		p, q = (), ()
		for i in range(len(p_x) - 1):
			delta_x = abs(p_x[i][0] - p_x[i+1][0])
			delta_y = abs(p_y[i][0] - p_y[i+1][0])
			if delta_x < old_delta_x:
				old_delta_x = delta_x
				p = (p_x[i], p_x[i+1])
			if delta_y < old_delta_y:
				old_delta_y = delta_y
				q = (p_y[i], p_y[i+1])
		distance_p = (p[0][0] - p[1][0])**2 + (p[0][1] - p[1][1])**2
		distance_q = (q[0][0] - q[1][0])**2 + (q[0][1] - q[1][1])**2
		if distance_p < distance_q:
			return p[0], p[1], distance_p
		else:
			return q[0], q[1], distance_q
	left, right = 0, len(p_x)
	mid = (right - left) // 2
	left_x, right_x = p_x[left:mid], p_x[mid:right]
	left_y, right_y = p_y[left:mid], p_y[mid:right]
	p1, q1, d1 = minimum_distance(left_x, left_y)
	p2, q2, d2 = minimum_distance(right_x, right_y)
	delta = min(d1, d2)
	p3, q3, d3 = closest_split_pair(p_x, p_y, delta)
	if p3 != () and q3 != ():
		if d1 < d2 and d1 < d3:
			return p1, q1, d1
		elif d2 < d1 and d2 < d3:
			return p2, q2, d2
		else:
			return p3, q3, d3
	else:
		if d1 < d2:
			return p1, q1, d1
		else:
			return p2, q2, d2

def main(x, y):
	p_x = sort_array(x, 0, len(x), y)
	p_y = sort_array(y, 0, len(y), x)
	point1, point2, dis = minimum_distance(p_x, p_y)
	print("{0:.9f}".format(math.sqrt(dis)))

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	main(x, y)