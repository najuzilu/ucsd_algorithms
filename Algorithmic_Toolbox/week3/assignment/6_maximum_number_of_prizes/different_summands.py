# Uses python3
import sys
import math

def optimal_summands(n):
	summands = []

	k = int(-1/2 + math.sqrt(1/4 + 2 * n))

	if k == 1:
		summands.append(n)
		return summands
	for each in range(1, k):
		summands.append(each)
	last_item = n - sum(summands)
	summands.append(last_item)
	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	print(len(summands))
	for x in summands:
		print(x, end=' ')
