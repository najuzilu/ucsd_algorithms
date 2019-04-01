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

	def siftDown(self, i):
		left_index = self.leftchild(i)
		right_index = self.rightchild(i)
		size = len(self.jobs)
		min_index = i
		if left_index < size and right_index < size: # node has left and right child
			# compare which of children nodes is smallest
			if self.jobs[left_index] < self.jobs[right_index]:
				min_index = left_index
			else:
				min_index = right_index
			if self.jobs[min_index] < self.jobs[i]: # swap
				self.jobs[min_index], self.jobs[i] = self.jobs[i], self.jobs[min_index]
				self.siftDown(min_index)
		elif left_index == size - 1: # node has only left child
			if self.jobs[left_index] < self.jobs[i]: # swap
				min_index = left_index
				self.jobs[left_index], self.jobs[i] = self.jobs[i], self.jobs[left_index]
				self.siftDown(min_index)

	def extractMin(self):
		if len(self.jobs) > 0:
			self.jobs[0], self.jobs[len(self.jobs)-1] = self.jobs[len(self.jobs)-1], self.jobs[0]
			result = self.jobs.pop()
			self.siftDown(0)
			return result
		return False


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

		## create a heap with number of m threads
		self.

		self.start_times = []
		self.assigned_workers = []

		start_time = 0

		while self.jobs: # while there are still jobs to process
			for i in range(self.num_workers):
				result = self.extractMin()
				#self.assigned_workers.append(i)
				#self.start_times.append(start_time)
				print(i, start_time)
				start_time = 
				


	def solve(self):
		self.read_data()
		self.assign_jobs()
		#self.write_response()

if __name__ == '__main__':
	job_queue = JobQueue()
	job_queue.solve()

