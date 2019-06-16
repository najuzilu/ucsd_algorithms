# Uses python3

def edit_distance(s, t): # i, j
	insertion, deletion, match, mismatch, min_val = 0, 0, 0, 0, 0

	matrix = [[] * (len(t) + 1)] * (len(s) + 1)
	matrix[0] = list(range(len(t) + 1)) # D(0, j) <- j for all j
	for i in range(1, len(s) + 1): # D(i, 0) <- i for all i
		matrix[i] = [i]

	for j in range(1, len(t) + 1):
		for i in range(1, len(s) + 1):
			new_array = matrix[i].copy()
			insertion = matrix[i][j - 1] + 1
			deletion = matrix[i - 1][j] + 1
			match = matrix[i - 1][j - 1]
			mismatch = matrix[i - 1][j - 1] + 1
			if s[i - 1] == t[j - 1]:
				min_val = min(insertion, deletion, match)
			else:
				min_val = min(insertion, deletion, mismatch)
			matrix[i].extend([min_val])
	return matrix[-1][-1]

if __name__ == "__main__":
	print(edit_distance(input(), input()))