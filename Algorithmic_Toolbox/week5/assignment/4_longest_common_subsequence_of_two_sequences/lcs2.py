#Uses python3
import sys

def edit_distance(a, b):
	insert, deletion, match, mismatch, min_val = 0, 0, 0, 0, 0

	edit_distance_matrix = [ [] * (len(b) + 1)] * (len(a) + 1)
	edit_distance_matrix[0] = list(range(len(b) + 1))
	for m in range(1, len(a) + 1):
		edit_distance_matrix[m] = [m]

	for j in range(1, len(b) + 1):
		for i in range(1, len(a) + 1):
			new_array = edit_distance_matrix[i].copy()
			insertion = edit_distance_matrix[i][j - 1] + 1
			deletion = edit_distance_matrix[i - 1][j] + 1
			match = edit_distance_matrix[i - 1][j - 1]
			mismatch = edit_distance_matrix[i - 1][j - 1] + 2
			if a[i - 1] == b[j - 1]:
				min_val = min(insertion, deletion, match)
			else:
				min_val = min(insertion, deletion, mismatch)
			edit_distance_matrix[i].extend([min_val])
	return edit_distance_matrix

def output_alignment(i, j, matrix):
	count = 0
	if i == 0 and j == 0:
		return count
	if i > 0 and matrix[i][j] == matrix[i - 1][j] + 1:
		count += output_alignment(i - 1, j, matrix)
	elif j > 0 and matrix[i][j] == matrix[i][j - 1] + 1:
		count += output_alignment(i, j - 1, matrix)
	else:
		count += output_alignment(i - 1, j - 1, matrix)
		if a[i - 1] == b[j - 1]:
			count += 1
	return count

def lcs2(a, b):
	ed_matrix = edit_distance(a, b)
	return output_alignment(len(a), len(b) , ed_matrix)

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))

	n = data[0]
	data = data[1:]
	a = data[:n]

	data = data[n:]
	m = data[0]
	data = data[1:]
	b = data[:m]

	print(lcs2(a, b))
