# Uses python3
import math

def evalt(a, b, op):
	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == '*':
		return a * b
	else:
		assert False

def min_and_max(M, m, i, j, string):
	min_val = math.inf
	max_val = - math.inf
	for k in range(i, j):
		a = evalt(M[i][k], M[k + 1][j], string[2 * k + 1])
		b = evalt(M[i][k], m[k + 1][j], string[2 * k + 1])
		c = evalt(m[i][k], M[k + 1][j], string[2 * k + 1])
		d = evalt(m[i][k], m[k + 1][j], string[2 * k + 1])
		min_val = min(min_val, a, b, c, d)
		max_val = max(max_val, a, b, c, d)
	return (min_val, max_val)

def get_maximum_value(dataset):
	n = math.ceil(len(dataset) / 2)
	min_matrix = [[None for _ in range(n)] for _ in range(n)]
	max_matrix = [[None for _ in range(n)] for _ in range(n)]
	for i in range(0, len(dataset), 2):
		if i == 0:
			min_matrix[i][i] = int(dataset[i])
			max_matrix[i][i] = int(dataset[i])
		else:
			min_matrix[i//2][i//2] = int(dataset[i])
			max_matrix[i//2][i//2] = int(dataset[i])
	for s in range(1, n):
		for i in range(n - s):
			j = i + s
			min_matrix[i][j], max_matrix[i][j] = min_and_max(max_matrix, min_matrix, i, j, dataset)
	return max_matrix[0][-1]

if __name__ == "__main__":
	print(get_maximum_value(input()))
