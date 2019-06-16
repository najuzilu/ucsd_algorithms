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
	n = m
	denominations = [3, 2, 1]
	min_num = [None] * (m + 1)
	min_num[0], min_num[1] = 0, 0
	results = []
	for i in range(2, m + 1):
		min_num[i] = math.inf 
		for j in range(len(denominations)):
			if i >= denominations[j]:
				if denominations[j] == 3 or denominations[j] == 2:
					if i % denominations[j] == 0:
						num_coin = min_num[i // denominations[j]] + 1
					else:
						num_coin = math.inf
				else:
					num_coin = min_num[i - 1] + 1
				if num_coin < min_num[i]:
					min_num[i] = num_coin

	while n > 0:
		min_value = math.inf
		next_value = n
		if min_num[n - 1] < min_value:
			min_value = min_num[n - 1]
			next_value = n - 1
		if n % 3 == 0:
			if min_num[n//3] < min_value:
				min_value = min_num[n//3]
				next_value = n // 3
		if n % 2 == 0:
			if min_num[n//2] <= min_value:
				min_value = min_num[n//2]
				next_value = n // 2
		results.append(n)
		n = next_value
	return min_num[m], reversed(results)

input = sys.stdin.read()
n = int(input)
# sequence = list(optimal_sequence(n))
k, sequence = get_change(n)
print(k)
for x in sequence:
	print(x, end=' ')