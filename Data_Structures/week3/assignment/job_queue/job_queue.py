# python3

class JobQueue:
	def read_data(self):
		# self.num_workers, m = map(int, input().split())
		# self.jobs = list(map(int, input().split()))
		self.num_workers, m = 2, 5
		self.jobs = [1, 2, 3, 4, 5]
		assert m == len(self.jobs)

	def write_response(self):
		for i in range(len(self.jobs)):
			print(self.assigned_workers[i], self.start_times[i])

	def parent(self, i):
		return int( (i+1) / 2)

	def leftchild(self, i):
		return 2*i + 1

	def rightchild(self, i):
		return 2*i + 2

	def siftDown(self, i, array):
		''' double check to see if it works for this case '''
		left_index = self.leftchild(i)
		right_index = self.rightchild(i)
		size = len(array)
		min_index = i
		if left_index < size and right_index < size: # node has left and right child
			# compare which of children nodes is smallest
			if array[left_index] < array[right_index]:
				min_index = left_index
			else:
				min_index = right_index
			if array[min_index] < array[i]: # swap
				array[min_index], array[i] = array[i], array[min_index]
				self.siftDown(min_index)
		elif left_index == size - 1: # node has only left child
			if array[left_index] < array[i]: # swap
				min_index = left_index
				array[left_index], array[i] = array[i], array[left_index]
				self.siftDown(min_index)

	def siftUp(self, i):
		''' basic idea - implement correctly '''
		while i > 1 and array[self.parent(i)] < array[i]:
			array[self.parent(i)], array[i] = array[i], array[self.parent(i)]
			i = self.parent(i)

	def changePriority(self, i, priority):
		''' basic idea - implement correctly '''
		old_priority = array[i]
		array[i] = priority
		if priority > old_priority:
			self.siftUp(i)
		else:
			self.siftDown(i)

	def assign_jobs(self):
		# TODO: replace this code with a faster algorithm.
		# self.assigned_workers = [None] * len(self.jobs)
		# self.start_times = [None] * len(self.jobs)
		# next_free_time = [0] * self.num_workers
		# for i in range(len(self.jobs)):
		# 	next_worker = 0
		# 	for j in range(self.num_workers):
		# 	if next_free_time[j] < next_free_time[next_worker]:
		# 		next_worker = j
		# 	self.assigned_workers[i] = next_worker
		# 	self.start_times[i] = next_free_time[next_worker]
		# 	next_free_time[next_worker] += self.jobs[i]

		# create a heap with number of m threads
		for i in range(self.num_workers):
			print(i)

	def solve(self):
		self.read_data()
		self.assign_jobs()
		#self.write_response()

if __name__ == '__main__':
	job_queue = JobQueue()
	job_queue.solve()

