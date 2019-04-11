#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree():
	if len(tree) > 0:
		return inOrder()
	else:
		return True


def inOrder(i = 0, value = 0):
	node = tree[i]
	# if node[0] <= node_value:
	# 	return False
	# else:
	# 	node_value = node[0]

	if node[1] != -1:
		left_child = tree[node[1]]
		# print('left_child {} - current {}'.format(left_child[0], node[0]))
		inOrder(node[1], value)
	print(node[0], value)
	if node[0] <= value:
		return False
	else:
		value = node[0]
	if node[2] != -1:
		right_child = tree[node[2]]
		# print('right_child {} - current {}'.format(left_child[0], node[0]))
		inOrder(node[2], value)


def main():
	# nodes = int(sys.stdin.readline().strip())
	# tree = []
	# for i in range(nodes):
	# 	tree.append(list(map(int, sys.stdin.readline().strip().split())))

	# Test 1	
	# global tree
	# nodes = 3
	# tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]

	# Test 2
	# global tree
	# nodes = 3
	# tree = [[1,1,2],[2,-1,-1],[3,-1,-1]]

	# Test 3
	# global tree
	# nodes = 0
	# tree = []

	# Test 4
	# global tree
	# nodes = 5
	# tree = [[1,-1,1],[2,-1,2],[3,-1,3],[4,-1,4],[5,-1,-1]]

	# nodes = 7
	# global tree
	# tree = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]

	nodes = 4
	global tree
	tree = [[4,1,-1],[2,2,3],[1,-1,-1],[5,-1,-1]]

	print(IsBinarySearchTree())

	# if IsBinarySearchTree():
	# 	print("CORRECT")
	# else:
	# 	print("INCORRECT")

threading.Thread(target=main).start()
