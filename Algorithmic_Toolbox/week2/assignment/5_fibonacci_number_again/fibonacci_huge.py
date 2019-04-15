# Uses python3
import sys

def calc_fib(n):
	array = [None] * (n + 1)
	if n == 0:
		return 0
	array[0] = 0
	array[1] = 1
	for i in range(2, n + 1):
		array[i] = array[i - 1] + array[i - 2]
	return array[n]

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

def get_fibonacci_huge(n, m):
	length_cycle = len(get_pisano_length(m))
	remainder = n % length_cycle
	return calc_fib(remainder) % m

if __name__ == '__main__':
	# input = input()
	input = sys.stdin.read()
	n, m = map(int, input.split())
	print(get_fibonacci_huge(n, m))
