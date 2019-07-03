#Uses python3
import math
import sys

def edit_distance(a, b, c):
	insert, deletion, match, mismatch, min_val = 0, 0, 0, 0, 0
	matrix = [[[math.inf for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

	for m in range(len(a) + 1):
		matrix[m][0][0] = m
	for n in range(1, len(b) + 1):
		matrix[0][n][0] = n
	matrix[0][0] = list(range(len(c) + 1))

	for ech in matrix:
		print(ech)

	# for k in range(1, len(c) + 1):
	# 	for j in range(1, len(b) + 1):
	# 		for i in range(1, len(a) + 1):
	# 			ins1 = matrix[i - 1][j][k] + 1
	# 			ins2 = matrix[i][j - 1][k] + 1
	# 			ins3 = matrix[i][j][k - 1] + 1
	# 			match = matrix[i - 1][j - 1][k - 1]
	# 			mismatch = matrix[i - 1][j - 1][k - 1] + 2
	# 			if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
	# 				min_val = min(ins1, ins2, ins3, match)
	# 			else:
	# 				min_val = min(ins1, ins2, ins3, mismatch)
	# 			matrix[i][j][k] = min_val

	return matrix[-1][-1][-1]

def lcs3(a, b, c):
	print('answer=', edit_distance(a, b, c))
	return min(len(a), len(b), len(c))

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
