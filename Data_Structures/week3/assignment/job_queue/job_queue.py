# python3

class JobQueue:
	def read_data(self):
		# self.num_workers, m = map(int, input().split())
		# self.jobs = list(map(int, input().split()))
		self.num_workers, m = 14, 3
		self.jobs = [2,11,6]
		assert m == len(self.jobs)

	def write_response(self):
		for i in range(len(self.jobs)):
			print(self.assigned_workers[i], self.start_times[i])

	def parent(self, k):
		return int( (k+1) / 2)

	def leftchild(self, k):
		return 2*k + 1

	def rightchild(self, k):
		return 2*k + 2

	def getMin(self):
		return self.heap[0]

	def siftDown(self, k):
		''' implement correctly '''
		minIndex = k
		leftIndex = self.leftchild(k)
		rightIndex = self.rightchild(k)
		size = len(self.heap)

		if leftIndex < size and rightIndex < size: # if left + right children
			''' checks left and right which is bigger '''
			left = self.heap[leftIndex]
			right = self.heap[rightIndex]
			if left[1] < right[1]:
				minIndex = leftIndex
			elif left[1] == right[1]: # choose one with smallest id
				if left[0] < right[0]:
					minIndex = leftIndex
				else:
					minIndex = rightIndex
			else:
				minIndex = rightIndex
			''' checks node with whichever child is bigger '''
			childMin = self.heap[minIndex]
			current = self.heap[k]
			if childMin[1] < current[1]:
				# swap and siftdown
				self.heap[minIndex], self.heap[k] = self.heap[k], self.heap[minIndex]
				self.siftDown(minIndex)
			elif childMin[1] == current[1]:
				if childMin[0] < current[0]:
					self.heap[minIndex], self.heap[k] = self.heap[k], self.heap[minIndex]
					self.siftDown(minIndex)
		elif leftIndex == size - 1: # node has only left child
			left = self.heap[leftIndex]
			current = self.heap[k]
			if left[1] < current[1]:
				self.heap[leftIndex], self.heap[k] = self.heap[k], self.heap[leftIndex]
				self.siftDown(leftIndex)
			elif left[1] == current[1]:
				if left[1] < current[0]:
					self.heap[leftIndex], self.heap[k] = self.heap[k], self.heap[leftIndex]
					self.siftDown(leftIndex)

	def siftUp(self, k):
		''' basic idea - implement correctly '''
		while k > 1 and self.heap[self.parent(k)] < self.heap[k]:
			self.heap[self.parent(k)], self.heap[k] = self.heap[k], self.heap[self.parent(k)]
			k = self.parent(k)

	def changePriority(self, k, priority):
		''' old priority is wrong '''
		old_priority = self.heap[k][1]
		self.heap[k][1] = priority
		if priority < old_priority:
			self.siftUp(k)
		else:
			self.siftDown(k)

	def assign_jobs(self):
		self.assigned_workers = [None] * len(self.jobs)
		self.start_times = [None] * len(self.jobs)

		self.heap = [] # first is id, next is priority 
		for i in range(self.num_workers):
			self.heap.append([i, 0])

		for i in range(len(self.jobs)):
			node = self.getMin() # always gets min value of priority
			id_ = node[0]
			result = node[1]
			self.assigned_workers[i] = id_
			self.start_times[i] = result
			self.changePriority(0, result + self.jobs[i]) # id of node , result

	def solve(self):
		self.read_data()
		self.assign_jobs()
		self.write_response()

if __name__ == '__main__':
	job_queue = JobQueue()
	job_queue.solve()

