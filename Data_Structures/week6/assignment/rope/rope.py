# python3

import sys

# Vertex of splay tree
class Vertex:
	def __init__(self, key, char, left, right, parent):
		(self.key, self.char, self.left, self.right, self.parent) = (key, char, left, right, parent)

class Rope:
	def __init__(self, s):
		self.s = s
		self.root = None
		for j in range(len(s)):
			self.insert(j, s[j])

	####### InOrderTraversal ########

	def inordertraversal(self, node):
		if node:
			if node.left:
				self.inordertraversal(node.left)
			print(node.key)
			if node.right:
				self.inordertraversal(node.right)

	################################

	def smallRotation(self, node):
		parent = node.parent
		if parent == None:
			return
		grandparent = node.parent.parent
		if parent.left == node:
			m = node.right
			node.right = parent
			parent.left = m 
		else:
			m = node.left
			node.left = parent
			parent.right = m 
		self.update(parent)
		self.update(node)
		node.parent = grandparent
		if grandparent != None:
			if grandparent.left == parent:
				grandparent.left = node
			else:
				grandparent.right = node

	def bigRotation(self, node):
		if node.parent.left == node and node.parent.parent.left == node.parent:
			# Zig-zig
			self.smallRotation(node.parent)
			self.smallRotation(node)
		elif node.parent.right == node and node.parent.parent.right == node.parent:
			# zig-zig
			self.smallRotation(node.parent)
			self.smallRotation(node)
		else:
			# Zig-zag
			self.smallRotation(node)
			self.smallRotation(node)


	def splay(self, node):
		if node == None:
			return None
		while node.parent != None:
			if node.parent.parent == None:
				self.smallRotation(node)
				break
			self.bigRotation(node)
		return node

	def find(self, root, key):
		node = root
		last = root
		next_node = None
		while node != None:
			if node.key >= key and (next_node == None or node.key < next_node.key):
				next_node = node
			last = node
			if node.key == key:
				break
			if node.key < key:
				node = node.right
			else:
				node = node.left
		root = self.splay(last)
		return (next_node, root)

	def update(self, node):
		if node == None:
			return
		node.key = node.key + (node.left.key if node.left != None else 0) + (node.right.key if node.right != None else 0)
		if node.left != None:
			node.left.parent = node
		if node.right != None:
			node.right.parent = node

	def merge(self, left, right):
		if left == None:
			return right
		if right == None:
			return left
		while right.left != None:
			right = right.left
		right = self.splay(right)
		right.left = left
		self.update(right)
		return right

	def split(self, root, key):
		(result, root) = self.find(root, key)
		if result == None:
			return (root, None)
		right = self.splay(result)
		left = right.left
		right.left = None
		if left != None:
			left.parent = None
		self.update(left)
		self.update(right)
		return (left, right)

	def insert(self, i, x):
		(left, right) = self.split(self.root, i)
		new_vertex = None
		if right == None or right.key != x:
			new_vertex = Vertex(i, x, None, None, None)
		self.root = self.merge(self.merge(left, new_vertex), right)

	def result(self):
		return self.s
		
	def process(self, i, j, k):
		# print(i, j, k, self.root)
		self.inordertraversal(self.root)
		pass

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
	break
print(rope.result())
