# python3
import sys

class SuffixTree(object):
	"""
		Suffix tree Implementation by Ben Langmead
		Link: https://nbviewer.jupyter.org/gist/BenLangmead/6665861
	"""
	class Node(object):
		def __init__(self, lab):
			self.lab = lab
			self.out = {}

	def __init__(self, s):
		s += '$'
		self.root = self.Node(None)
		self.root.out[s[0]] = self.Node(s)

		for i in range(1, len(s)):
			cur = self.root
			j = i
			while j < len(s):
				if s[j] in cur.out:
					child = cur.out[s[j]]
					lab = child.lab
					k = j + 1
					while k - j < len(lab):
						k += 1
					if k - j == len(lab):
						cur = child
						j = k
					else:
						cExist, cNew = lab[k-j], s[k]
						mid = self.Node(lab[:k-j])
						mid.out[cNew] = self.Node(s[k:])
						mid.out[cExist] = child
						child.lab = lab[k-j:]
						cur.out[s[j]] = mid
				else:
					cur.out[s[j]] = self.Node(s[j:])

	def followPath(self, s):
		cur = self.root
		i = 0

		while i < len(s):
			c = s[i]
			if c not in cur.out:
				return (None, None)
			child = cur.out[s[i]]
			lab = child.lab
			j = i + 1
			while j - i < len(lab) and j < len(s) and s[j] == lab[j-i]:
				j += 1
			if j - i == len(lab):
				cur = child
				i = j
			elif j == len(s):
				return (child, j - i)
			else:
				return (None, None)
		return (cur, None)

	def hasSubstring(self, s):
		node, off = self.followPath(s)
		return node is not None

	def hasSuffix(self, s):
		node, off = self.followPath(s)
		if node is None:
			return False
		if off is None:
			return '$' in node.out
		else:
			return node.lab[off] == '$'


if __name__ == '__main__':
	text = 'AAATG'
	stree = SuffixTree(text)
	print(stree.hasSuffix('ATG'))