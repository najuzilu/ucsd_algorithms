class createHeap(object):
    def __init__(self, n, lines):
        self.heap = []
        for i in range(n):
            self.heap.append([i, 0, lines[i]])
        self.copy_heap = self.heap.copy()
        self.GenerateSwaps()
        print(self.copy_heap)

    def getHeap(self):
        return self.heap

    def getMax(self):
        return self.copy_heap[0]

    def GenerateSwaps(self):
        mid_bound = int(len(self.copy_heap)/2)
        for i in range(mid_bound, -1, -1):
            self.siftDown(i)

    def parentIndex(self, i):
        return int((i + 1) / 2)

    def leftchild(self, i):
        return 2*i + 1

    def rightchild(self, i):
        return 2*i + 2

    def siftDown(self, k):
        maxIndex = k
        leftIndex = self.leftchild(k)
        rightIndex = self.rightchild(k)
        size = len(self.copy_heap)
        current = self.copy_heap[k]
        if leftIndex < size and rightIndex < size: # if left + right children
            left = self.copy_heap[leftIndex]
            right = self.copy_heap[rightIndex]
            if left[2] > current[2]:
                if left[2] > right[2]:
                    maxIndex = leftIndex
                else:
                    maxIndex = rightIndex
                self.copy_heap[maxIndex], self.copy_heap[k] = self.copy_heap[k], self.copy_heap[maxIndex]
                self.siftDown(maxIndex)
            elif right[2] > current[2]:
                maxIndex = rightIndex
                self.copy_heap[maxIndex], self.copy_heap[k] = self.copy_heap[k], self.copy_heap[maxIndex]
                self.siftDown(maxIndex)
        elif leftIndex == size - 1: # node has only left child
            left = self.copy_heap[leftIndex]
            if left[2] > current[2]:
                maxIndex = leftIndex
                self.copy_heap[leftIndex], self.copy_heap[k] = self.copy_heap[k], self.copy_heap[leftIndex]
                self.siftDown(maxIndex)        

    def siftUp(self, k):
        while k > 1 and self.copy_heap[self.parent(k)][2] < self.copy_heap[k][2]:
            self.heap[self.parent(k)], self.heap[k] = self.heap[k], self.heap[self.parent(k)]
            k = self.parent(k)

    def changePriority(self, k, priority):
        old_priority = self.heap[k][2]
        self.heap[k][2] = priority
        if priority < old_priority:
            self.siftUp(k)
        else:
            self.siftDown(k)