# python3
import sys

def count_iterations(text_length):
	countDict = {}
	for i in range(len(text_length)):
		element = text_length[i]
		if element not in countDict.keys():
			countDict[element] = 1
		else:
			countDict[element] += 1
	return (countDict, countDict.copy())

def map_first_to_last(bwt, firstCol):
	matrix = {}
	firstColCount,lastColCount = count_iterations(bwt)
	for i in range(len(firstCol)):
		firstElement = firstCol[i]
		lastElement = bwt[i]
		matrix[firstElement + str(firstColCount[firstElement])] = lastElement + str(lastColCount[lastElement])
		firstColCount[firstElement] -= 1
		lastColCount[lastElement] -= 1
	return matrix

def InverseBWT(bwt):
	result = ''
	init_text = '$1'

	firstCol = ''.join(sorted(bwt)) # sorted bwt
	lastToFirstMatrix = map_first_to_last(bwt, firstCol)
	
	for i in range(len(firstCol)):
		init_text = lastToFirstMatrix[init_text]
		result += init_text[0]
	result = result[:-1]
	result = result[::-1]
	return result + '$'

if __name__ == '__main__':
	bwt = sys.stdin.readline().strip()
	print(InverseBWT(bwt))