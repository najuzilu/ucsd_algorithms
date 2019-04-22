# Uses python3
import sys

def get_change(m):
	remainder_10 = m // 10
	m = m - (remainder_10 * 10)

	remainder_5 = m // 5
	m = m - (remainder_5 * 5)
	
	return remainder_10 + remainder_5 + m

if __name__ == '__main__':
	m = int(sys.stdin.read())
	# m = int(input())
	print(get_change(m))
