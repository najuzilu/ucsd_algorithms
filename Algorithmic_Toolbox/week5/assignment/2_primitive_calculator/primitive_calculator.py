# Uses python3
import sys
import math

def optimal_sequence(n):
	sequence = []
	while n >= 1:
		sequence.append(n)
		if n % 3 == 0:
			n = n // 3
		elif n % 2 == 0:
			n = n // 2
		else:
			n = n - 1
	return reversed(sequence)

def get_change(m):
	denominations = [3, 2, 1]
	min_num = [None] * (m + 1)
	min_num[0], min_num[1] = 0, 0

	results = []
	results.append(1)

	for i in range(2, m + 1):
		min_num[i] = math.inf 
		for j in range(len(denominations)):
			if i >= denominations[j]:
				if denominations[j] == 3:
					if i % denominations[j] == 0:
						num_coin = min_num[i // 3] + 1
					else:
						num_coin = math.inf
				elif denominations[j] == 2:
					if i % denominations[j] == 0:
						num_coin = min_num[i // 2] + 1
					else:
						num_coin = math.inf
				else:
					num_coin = min_num[i - 1] + 1
				if num_coin < min_num[i]:
					min_num[i] = num_coin
					
	for i in range(1, len(min_num) - 1):
		if (min_num[i + 1] == min_num[i] + 1) or (min_num[i + 1] == 2 * min_num[i]) or (min_num[i + 1] == 3 * min_num[i]):
			results.append(i)
	return min_num[m], results

input = sys.stdin.read()
n = int(input)
# sequence = list(optimal_sequence(n))
k, sequence = get_change(n)
print(k)
for x in sequence:
	print(x, end=' ')