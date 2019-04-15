# Uses python3
import sys

def calc_fib(n1, n2):
	answer = 0
	array = []
	if n2 == 0:
		return 0
	array.append(0)
	array.append(1)
	if n1 <= 1:
		answer += 1
	for i in range(2, n2 + 1):
		array.append((array[i - 1] + array[i - 2]))
		if i >= n1:
			answer += array[i]
	return answer

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

def fibonacci_sum(n1, n2):
	m = 10
	length_cycle = len(get_pisano_length(m))

	remainder2 = n2 % length_cycle
	remainder1 = n1 % length_cycle
	return calc_fib(remainder1, remainder2) % m

def fibonacci_partial_sum(from_, to):
	return fibonacci_sum(from_, to)

if __name__ == '__main__':
	input = sys.stdin.read()
	# input = input()
	from_, to = map(int, input.split())
	print(fibonacci_partial_sum(from_, to))