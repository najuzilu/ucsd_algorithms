# Uses python3
import sys
# sys.setrecursionlimit(1500)

def binary_search(a, x, left_idx, right_idx):
	if right_idx <= left_idx:
		return -1
	mid_idx = int(left_idx + (right_idx - left_idx)/2)
	if x == a[mid_idx]:
		return mid_idx
	elif x < a[mid_idx]:
		if right_idx - left_idx == 1: return -1
		right_idx = mid_idx
		return binary_search(a, x, left_idx, right_idx)
	elif x > a[mid_idx]:
		if right_idx - left_idx == 1: return -1
		left_idx = mid_idx
		return binary_search(a, x, left_idx, right_idx)

def linear_search(a, x):
	for i in range(len(a)):
		if a[i] == x:
			return i
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	m = data[n + 1]
	a = data[1 : n + 1]
	left_idx, right_idx = 0, len(a)
	for x in data[n + 2:]:
		print(binary_search(a, x, left_idx, right_idx), end = ' ')
	# 	print(linear_search(a, x), end = ' ') # linear_search implementation
