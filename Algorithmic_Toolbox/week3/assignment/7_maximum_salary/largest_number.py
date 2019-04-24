#Uses python3

import sys

def largest_number(a):
	res = ""
	# a.sort(key = lambda item: item[0], reverse = True)
	
	while a != []:
		maxDigit = '0'
		for digit in a:
			if digit[0] > maxDigit[0]:
				maxDigit = digit
			elif digit[0] == maxDigit[0]:
				if len(digit) < len(maxDigit):
					maxDigit = digit
		res += maxDigit
		a.remove(maxDigit)
	return res

if __name__ == '__main__':
	input = sys.stdin.read()
	data = input.split()
	a = data[1:]
	print(largest_number(a))