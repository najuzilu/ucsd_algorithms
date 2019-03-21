# python3

import sys
import threading

class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

class TreeHeight(object):

    def __init__(self, n, parent):
        self.n = n
        self.parent = parent

    def get_height(self, node):
        

    def compute(self):
        node_array = []
        for i in range(self.n):
            node_array.append(Node(i))

        for j in range(len(node_array)):
            if self.parent[j] == -1:
                root = node_array[j]
            else:
                node_array[self.parent[j]].children.append(node_array[j])
        return self.get_height(root)


def main():
    n = int(input())
    parent = list(map(int, input().split()))
    c = TreeHeight(n, parent)
    c.get_height()

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
