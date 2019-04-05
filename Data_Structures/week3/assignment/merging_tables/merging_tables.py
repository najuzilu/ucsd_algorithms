# python3

import sys

class MaxHeap(object):
    def __init__(self, table):
        self.heap = table

    def parentIndex(self, i):
        return int((i+1)/2)

    def leftchildIndex(self, i):
        return 2*i + 1

    def rightchildIndex(self, i):
        return 2*i + 2

    def getMax(self):
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
                if left[0] < current[0]:
                    self.heap[leftIndex], self.heap[k] = self.heap[k], self.heap[leftIndex]
                    self.siftDown(leftIndex)

    def siftUp(self, k):
        ''' basic idea - implement correctly '''
        while k > 1 and self.heap[self.parent(k)] < self.heap[k]:
            self.heap[self.parent(k)], self.heap[k] = self.heap[k], self.heap[self.parent(k)]
            k = self.parent(k)

    def GenerateSwaps(self):
        mid_bound = int(len(self._data)/2)
        for i in range(mid_bound, -1, -1):
            self.siftDown(i)


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))

rank = [1] * n
parent = list(range(0, n))

def getParent(entry):
    if entry != parent[entry]:
        parent[entry] = getParent(parent[entry])
    return parent[entry]

def merge(destination, source):
    input1, input2 = getParent(destination), getParent(source)

    if input1 == input2:
        return False

    if rank[input1] > rank[input2]:
        parent[input2] = input1
        lines[input1] += lines[source]
    else:
        parent[input1] = input2
        lines[input2] += lines[input1]
        if rank[input1] == rank[input2]:
            rank[input2] += 1
    return True

'''
    # Stress Test Implementation
with open('./tests/116.a') as f:
    test = f.read().splitlines()

for i in range(100000):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    #print(lines)
    if max(lines) != int(test[i]):
        print('ERROR >> max(lines)={} test[i]={}'.format(max(lines),test[i]))
'''

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    # have a different implementation than max(lines)