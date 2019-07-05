# Uses python3
import sys
import itertools

def partition3_naive(A):
	for c in itertools.product(range(3), repeat=len(A)):
		sums = [None] * 3
		for i in range(3):
			sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

		if sums[0] == sums[1] and sums[1] == sums[2]:
			return 1
	return 0

def optimal_weight(W, n):
	count = 0
	matrix = [[0 for _ in range(W + 1)] for _ in range(len(n) + 1)]
	for i in range(1, len(n) + 1):
		for j in range(1, W + 1):
			matrix[i][j] = matrix[i - 1][j]
			if n[i - 1] <= j:
				val = matrix[i - 1][j - n[i - 1]] + n[i - 1]
				if matrix[i][j] < val:
					matrix[i][j] = val
			if matrix[i][j] == W: count += 1
	if count < 3:
		return 0
	else:
		return 1

def partition3(A):
	k = 3 # we need to form 3 subsets
	total_sum = sum(A)
	if total_sum % k == 0:
		partial_sum = total_sum // 3
		return optimal_weight(partial_sum, A)
	else:
		return 0

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *A = list(map(int, input.split()))
	print(partition3(A))

