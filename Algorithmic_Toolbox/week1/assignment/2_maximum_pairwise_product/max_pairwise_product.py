# python3

def max_pairwise_product(numbers):
	n = len(numbers)
	max_product = 0

	firstMax = 0
	for i in range(len(numbers)):
		if numbers[i] > firstMax:
			firstMax = numbers[i]
			numbers[0], numbers[i] = numbers[i], numbers[0] # swap

	secondMax = 0
	for j in range(1, len(numbers)):
		if numbers[j] > secondMax:
			secondMax = numbers[j]
			numbers[1], numbers[j] = numbers[j], numbers[1] # swap

	max_product = firstMax * secondMax
	return max_product

def even_faster_max_pairwise_product(numbers):
	return


if __name__ == '__main__':
	input_n = int(input())
	input_numbers = [int(x) for x in input().split()]
	print(max_pairwise_product(input_numbers))