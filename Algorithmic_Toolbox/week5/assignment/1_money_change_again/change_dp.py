# Uses python3
import sys
import math

def get_change(m):
	denominations = [1, 3, 4]
	min_num_coins = [None] * (m + 1)
	min_num_coins[0] = 0

	for i in range(1, m + 1):
		min_num_coins[i] = math.inf 
		for j in range(len(denominations)):
			if i >= denominations[j]:
				num_coin = min_num_coins[i - denominations[j]] + 1
				if num_coin < min_num_coins[i]:
					min_num_coins[i] = num_coin
	return min_num_coins[m]

if __name__ == '__main__':
	m = int(sys.stdin.read())
	print(get_change(m))