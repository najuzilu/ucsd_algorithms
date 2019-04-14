# Uses python3
import sys

def fibonacci_sum(n):
	if n <= 1:
		return n
	array = [None] * (n + 1)
	array[0] = 0
	array[1] = 1
	answer = 1
	for i in range(2, n + 1):
		array[i] = (array[i - 1] + array[i - 2]) % 10
	return array[n]

if __name__ == '__main__':
	# input = sys.stdin.read()
	# n = int(input)
	n = int(input())
	print(fibonacci_sum(n))
	print(get_fibonacci_huge(n-1, 10), get_fibonacci_huge(n-2, 10), get_fibonacci_huge(n, 10))
