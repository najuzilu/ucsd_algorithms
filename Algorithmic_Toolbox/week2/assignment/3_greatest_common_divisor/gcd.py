# Uses python3
import sys

def gcd(a, b):
	if b == 0:
		return a
	a_ = a % b
	return gcd(b, a_)

if __name__ == "__main__":
	# input = input() # for cli testing
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(gcd(a, b))