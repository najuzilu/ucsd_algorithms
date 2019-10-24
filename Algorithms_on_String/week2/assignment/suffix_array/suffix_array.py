# python3
import sys

def buildSuffixArray(text):
	"""
	Build suffix array of the string text and
	return a list result of the same length as the text
	such that the value result[i] is the index (0-based)
	in text where the i-th lexicographically smallest
	suffix of text starts.
	"""
	result = []
	textCount, mapping = {}, {}

	for i in range(len(text)):
		if text[i] not in textCount.keys():
			textCount[text[i]] = 1
		else:
			textCount[text[i]] += 1
		mapping[text[i:len(text)]] = i

	for key in sorted(mapping.keys()):
		result.append(mapping[key])
	return result

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	print(" ".join(map(str, buildSuffixArray(text))))