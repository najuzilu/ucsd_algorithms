# Uses python3
import sys

def gcd(a, b):
	if b == 0:
		return a
	a_ = a % b
	return gcd(b, a_)

def lcm_naive(a, b):
	return a*b // gcd(a, b)

if __name__ == '__main__':
	# input = input()
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(lcm_naive(a, b))

