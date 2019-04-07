# python3

import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def areEqual(string1, string2):
	for i in range(len(string1) - 1):
		if string1[i] != string2[i]:
			return False 
	return True

def polyHash(pattern, prime, x):
	'''
		prime is int greater than 10**8
		x is random int between [1, prime - 1]
	'''
	hashVal = 0
	for i in range( len(pattern) - 1, -1, -1):
		hashVal = (hashVal * x + ord(pattern[i])) % prime
	return hashVal

def precomputeHashes(text, len_pattern, prime, x):
	'''
		text is actual text input
		len_pattern is the length of the pattern
		prime is int greater than 10**8
		x is a random int between [1, prime - 1]
	'''
	# Step 2: create the answer array with the length of the difference + 1
	H = [None] * (len(text) - len_pattern + 1)
	# Step 3: get string which contains only the "last string"
	S = text[len(text) - len_pattern:]
	# Step 4: generate the polyHash of the last entry
	H[len(text) - len_pattern] = polyHash(S, prime, x)
	# Step 5: create y = x**|P|
	y = 1
	for i in range(len_pattern):
		y = (y * x) % prime
	# Step 6: create result array
	for i in range(len(text) - len_pattern - 1, -1, -1):
		#H[i] = ( x * H[i+1] + ord(text[i]) - y * ord(text[i+len_pattern]) + prime ) % prime
		H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + len_pattern]) + prime) % prime
	return H

def get_occurrences(pattern, text):
	# Step 1: set prime larger than 10**8 and choose a random int x such that x is [1, prime-1]
	prime = 100000009
	x = random.randint(1, prime - 1)
	# Step 2: calculate array where the results of the indexes will be stored
	result = []
	# Step 3: calculate hash of pattern
	pHash = polyHash(pattern, prime, x)
	# Step 4: precompute hashes
	H = precomputeHashes(text, len(pattern), prime, x)
	# Step 5: check to see if hashes are the same and if they are the same whether it is a false positive
	for i in range(len(text) - len(pattern) + 1):
		if pHash == H[i] and areEqual(text[i:i+len(pattern)-1], pattern):
			result.append(i)
	return result
	

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))