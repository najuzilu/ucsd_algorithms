#Uses python3
import math
import sys

def edit_distance(a, b, c):
	matrix = [[[0 for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

	for k in range(1, len(c) + 1):
		for j in range(1, len(b) + 1):
			for i in range(1, len(a) + 1):
				if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
					matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
				else:
					matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])
	return matrix[-1][-1][-1]

def lcs3(a, b, c):
	return edit_distance(a, b, c)

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	an = data[0]
	data = data[1:]
	a = data[:an]
	data = data[an:]
	bn = data[0]
	data = data[1:]
	b = data[:bn]
	data = data[bn:]
	cn = data[0]
	data = data[1:]
	c = data[:cn]
	print(lcs3(a, b, c))
