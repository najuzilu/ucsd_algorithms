# Uses python3
import sys

def optimal_weight(W, n):
	matrix = [[0 for _ in range(W + 1)] for _ in range(len(n) + 1)]
	for i in range(1, len(n) + 1):
		for j in range(1, W + 1):
			matrix[i][j] = matrix[i - 1][j]
			if n[i - 1] <= j:
				val = matrix[i - 1][j - n[i - 1]] + n[i - 1]
				if matrix[i][j] < val:
					matrix[i][j] = val
	return matrix[-1][-1]

if __name__ == '__main__':
	input = sys.stdin.read()
	W, n, *w = list(map(int, input.split()))
	print(optimal_weight(W, w))
