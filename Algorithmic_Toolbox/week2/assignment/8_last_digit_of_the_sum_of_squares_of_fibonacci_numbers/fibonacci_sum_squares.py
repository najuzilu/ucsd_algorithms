# Uses python3
from sys import stdin

def calc_fib(n):
	array = []
	if n == 0:
		return 0
	array.append(0)
	array.append(1)
	for i in range(2, n + 2):
		array.append((array[i - 1] + array[i - 2]))
	return array[n] * array[n + 1]

def get_pisano_length(n):
	array = []
	if n < 1:
		return n
	array.append(0)
	array.append(1)
	for i in range(2, n*n + 1):
		next_ = (array[i - 1] + array[i - 2]) % n
		if (array[i-1] == 0) and (next_ == 1):
			array.pop()
			break
		else:
			array.append(next_)
	return array

def fibonacci_sum(n):
	m = 10
	length_cycle = len(get_pisano_length(m))
	remainder = n % length_cycle
	return calc_fib(remainder) % m

def fibonacci_sum_squares(n):
	return fibonacci_sum(n)

if __name__ == '__main__':
	n = int(stdin.read())
	# n = int(input())
	print(fibonacci_sum_squares(n))
