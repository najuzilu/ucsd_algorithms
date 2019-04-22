# Uses python3

# python fractional_knapsack.py < tests/1

import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	# calculate value per 1 weight
	val_per_weight = [x/y for x, y in zip(values, weights)]
	
	while capacity != 0 and len(val_per_weight) != 0:
		index_max = val_per_weight.index(max(val_per_weight))

		if weights[index_max] / capacity <= 1:
			capacity = capacity - weights[index_max]
			value += values[index_max]
			# pop items and continue while loop
			weights.pop(index_max)
			values.pop(index_max)
			val_per_weight.pop(index_max)
		else:
			value += (capacity / weights[index_max]) * values[index_max]
			capacity -= capacity
	return value


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))
