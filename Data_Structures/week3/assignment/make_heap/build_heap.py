# python3

class HeapBuilder:
	def __init__(self):
		self._swaps = []
		self._data = []

	def ReadData(self):
		n = int(input())
		self._data = [int(s) for s in input().split()]
		assert n == len(self._data)

	def WriteResponse(self):
		print(len(self._swaps))
		for swap in self._swaps:
			print(swap[0], swap[1])

	def parentIndex(self, i):
		return int((i+1)/2)

	def leftchildIndex(self, i):
		return 2*i + 1

	def rightchildIndex(self, i):
		return 2*i + 2

	def siftDown(self, i):
		left_index = self.leftchildIndex(i)
		right_index = self.rightchildIndex(i)
		size = len(self._data)
		min_index = i
		if left_index < size and right_index < size: # node has left and right child
			# compare which of children nodes is smallest
			if self._data[left_index] < self._data[right_index]:
				min_index = left_index
			else:
				min_index = right_index
			if self._data[min_index] < self._data[i]: # swap
				self._swaps.append([i, min_index])
				self._data[min_index], self._data[i] = self._data[i], self._data[min_index]
				self.siftDown(min_index)
		elif left_index == size - 1: # node has only left child
			if self._data[left_index] < self._data[i]: # swap
				min_index = left_index
				self._swaps.append([i, min_index])
				self._data[left_index], self._data[i] = self._data[i], self._data[left_index]
				self.siftDown(min_index)

	def GenerateSwaps(self):
		mid_bound = int(len(self._data)/2)
		for i in range(mid_bound, -1, -1):
			self.siftDown(i)

	def Solve(self):
		self.ReadData()
		self.GenerateSwaps()
		self.WriteResponse()

if __name__ == '__main__':
	heap_builder = HeapBuilder()
	heap_builder.Solve()
