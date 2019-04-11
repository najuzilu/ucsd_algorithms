#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree():
	if len(tree) > 0:
		return inOrder()
	else:
		return True


def inOrder(i = 0):
	global prev_value
	node = tree[i]

	if node[1] != -1:
		left_child = tree[node[1]]
		inOrder(node[1])

	# print(node[0], prev_value)
	if node[0] <= prev_value:
		return False
	else:
		prev_value = node[0]

	if node[2] != -1:
		right_child = tree[node[2]]
		inOrder(node[2])
	return True


def main():
	# nodes = int(sys.stdin.readline().strip())
	# global tree
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

	# Test 5
	# nodes = 7
	# global tree
	# tree = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]

	# Test 6
	# nodes = 4
	# global tree
	# tree = [[4,1,-1],[2,2,3],[1,-1,-1],[5,-1,-1]]

	# Test 7
	# nodes = 3
	# global tree
	# tree = [[-887440904, -1, 1], [-887440903, -1, 2], [-13646870, -1, -1]]

	# Test 8
	# nodes = 7
	# global tree
	# tree = [[4, 1, 2],[2, 3, 4],[6, 5, 6],[1, -1, -1],[3, -1, -1],[4, -1, -1],[7, -1, -1]]

	# Test 9
	# nodes = 2
	# global tree
	# tree = [[2147483647, -1, 1], [2147483647, -1, -1]]

	# Test 10
	# nodes = 2
	# global tree
	# tree = [[-2147483648, 1, -1],[-2147483648, -1, -1]]

	global prev_value
	prev_value = -float("inf")
	if IsBinarySearchTree():
		print("CORRECT")
	else:
		print("INCORRECT")

threading.Thread(target=main).start()
