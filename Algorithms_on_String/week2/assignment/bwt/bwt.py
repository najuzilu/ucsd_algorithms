# python3
import sys

def BWT(text):
	array = []
	result = ''
	for i in range(len(text)):
		text = text[-1] + text[:-1]
		array.append(text)
	sorted_array = sorted(array)
	for each in sorted_array:
		result += each[-1]
	return result

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	print(BWT(text))