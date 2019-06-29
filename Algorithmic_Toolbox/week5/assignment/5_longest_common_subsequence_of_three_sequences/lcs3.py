#Uses python3
import math
import sys

def edit_distance(a, b, c):
	insert, deletion, match, mismatch, min_val = 0, 0, 0, 0, 0
	matrix = [ [ [math.inf] * (len(c) + 1)] * (len(b) + 1)] * (len(a) + 1)

	# for m in range(len(a) + 1):
		# matrix[m] = [[m]]
	# for n in range(1, len(b) + 1):
	# 	matrix[0].append([n])
	# matrix[0][0] = list(range(len(c) + 1))


	# matrix[0][0] = list(range(len(c) + 1))

	
	
	print('\n',matrix)

	# for k in range(1, len(c) + 1):
	# 	for j in range(1, len(b) + 1):
	# 		for i in range(1, len(a) + 1):
	# 			insertion = matrix[i - 1][j - 1][k] + 1
	# 			deletion = matrix[i][j - 1][k - 1] + 1
	# 			ins_del = matrix[i - 1][j][k - 1] + 1
	# 			match = matrix[i - 1][j - 1][k - 1]
	# 			mismatch = matrix[i - 1][j - 1][k - 1] + 2
	# 			if a[i] == b[j] == c[k]:
	# 				min_val = min(insertion, deletion, ins_del, match)
	# 			else:
	# 				min_val = min(insertion, deletion, ins_del, mismatch)
	# 			print(matrix[i], min_val, i, j, k)
	# 			break
	# 		break
	# 	break
				
				





	# edit_distance_matrix[0] = list(range(len(b) + 1))
	# for m in range(1, len(a) + 1):
	# 	edit_distance_matrix[m] = [m]

	# for j in range(1, len(b) + 1):
	# 	for i in range(1, len(a) + 1):
	# 		new_array = edit_distance_matrix[i].copy()
	# 		insertion = edit_distance_matrix[i][j - 1] + 1
	# 		deletion = edit_distance_matrix[i - 1][j] + 1
	# 		match = edit_distance_matrix[i - 1][j - 1]
	# 		mismatch = edit_distance_matrix[i - 1][j - 1] + 2
	# 		if a[i - 1] == b[j - 1]:
	# 			min_val = min(insertion, deletion, match)
	# 		else:
	# 			min_val = min(insertion, deletion, mismatch)
	# 		edit_distance_matrix[i].extend([min_val])
	return 

def lcs3(a, b, c):
	edit_distance(a, b, c)
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
