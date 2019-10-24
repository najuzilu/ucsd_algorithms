# python3
import sys

def firstOccurance(string):
	dict_ = {}
	string = sorted(string)
	previousStr = string[0]
	dict_[string[0]] = 0
	for i in range(1, len(string)):
		if string[i] != previousStr:
			dict_[string[i]] = i
		previousStr = string[i]
	return dict_

def PreprocessBWT(bwt):
	"""
		Preprocess the Burrows-Wheeler Transform bwt of some text and compute as a result:
			* starts - for each character C in bwt, starts[C] is the first position of this character in the sorted array of  all characters of the text.
			* occ_count_before - for each character C in bwt and each position P in bwt, occ_count_before[C][P] is the number of occurrences of character C in bwt from position 0 to position P inclusive.
	"""
	occ_counts_before = []
	dictRow = {k: 0 for k in set(sorted(bwt))}

	startsDict = firstOccurance(bwt)
	for char in bwt:
		occ_counts_before.append(dictRow.copy())
		dictRow[char] += 1
	occ_counts_before.append(dictRow.copy())
	return startsDict, occ_counts_before

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
	"""
	Compute the number of occurrences of string pattern in the text
	given only Burrows-Wheeler Transform bwt of the text and additional
	information we get from the preprocessing stage - starts and occ_counts_before.
	"""
	top = 0
	bottom = len(bwt) - 1

	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]

			# if (occ_counts_before[top][symbol] > 0) or (occ_counts_before[bottom][symbol] - 1 > 0):
			if symbol in occ_counts_before[top].keys():
				top = starts[symbol] + occ_counts_before[top][symbol]
				bottom = starts[symbol] + occ_counts_before[bottom + 1][symbol] - 1
			else:
				return 0
		else:
			return bottom - top + 1
	return 0


if __name__ == '__main__':
	bwt = sys.stdin.readline().strip()
	pattern_count = int(sys.stdin.readline().strip())
	patterns = sys.stdin.readline().strip().split()
	
	# Preprocess the BWT once to get starts and occ_count_before.
	# For each pattern, we will then use these precomputed values and
	# spend only O(|pattern|) to find all occurrences of the pattern
	# in the text instead of O(|pattern| + |text|).

	starts, occ_counts_before = PreprocessBWT(bwt)
	occurrence_counts = []
	for pattern in patterns:
		occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
	print(' '.join(map(str, occurrence_counts)))
