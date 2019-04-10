# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.key = [0 for i in range(self.n)]
		self.left = [0 for i in range(self.n)]
		self.right = [0 for i in range(self.n)]
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a
			self.left[i] = b
			self.right[i] = c

		# Example 1
		# self.n = 5
		# self.key = [4, 2, 5, 1, 3]                 
		# self.left = [1, 3, -1, -1, -1]
		# self.right = [2, 4, -1, -1, -1]

		# Example 2
		# self.n = 10
		# self.key = [0,10,20,30,40,50,60,70,80,90]
		# self.left = [7,-1,-1,8,3,-1,1,5,-1,-1]
		# self.right = [2,-1,6,9,-1,-1,-1,4,-1,-1]

	def InOrderTraversal(self, iter_):
		if self.left[iter_] != -1:
			if self.InOrderTraversal(self.left[iter_]):
				self.result.append(self.InOrderTraversal(self.left[iter_]))
		self.result.append(self.key[iter_])
		if self.right[iter_] != -1:
			if self.InOrderTraversal(self.right[iter_]):
				self.result.append(self.InOrderTraversal(self.right[iter_]))

	def PreOrderTraversal(self, iter_):
		self.result.append(self.key[iter_])
		if self.left[iter_] != -1:
			if self.PreOrderTraversal(self.left[iter_]):
				self.result.append(self.PreOrderTraversal(self.left[iter_]))
		if self.right[iter_] != -1:
			if self.PreOrderTraversal(self.right[iter_]):
				self.result.append(self.PreOrderTraversal(self.right[iter_]))

	def PostOrderTraversal(self, iter_):
		if self.left[iter_] != -1:
			if self.PostOrderTraversal(self.left[iter_]):
				self.result.append(self.PostOrderTraversal(self.left[iter_]))
		if self.right[iter_] != -1:
			if self.PostOrderTraversal(self.right[iter_]):
				self.result.append(self.PostOrderTraversal(self.right[iter_]))
		self.result.append(self.key[iter_])

	def inOrder(self):
		self.result = []
		if self.key == []:
			return
		self.InOrderTraversal(0)
		return self.result

	def preOrder(self):
		self.result = []
		if self.key == []:
			return
		self.PreOrderTraversal(0)
		return self.result

	def postOrder(self):
		self.result = []
		if self.key == []:
			return
		self.PostOrderTraversal(0)
		return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
