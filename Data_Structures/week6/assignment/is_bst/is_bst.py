#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


def IsBinarySearchTree():
	global tree
	if len(tree) > 1:
		if inOrder() == None:
			return True
		else:
			return False
	else:
		return True

def inOrder(i = 0):
	global tree
	global prev_value

	node = tree[i]

	if node[1] != -1:
		inOrder(node[1])

	print(node[0], prev_value)
	if node[0] <= prev_value:
		return False
	else:
		prev_value = node[0]

	if node[2] != -1:
		inOrder(node[2])

def main():
	global tree

	nodes = int(sys.stdin.readline().strip())
	tree = []
	for i in range(nodes):
		tree.append(list(map(int, sys.stdin.readline().strip().split())))

	if IsBinarySearchTree():
		print("CORRECT")
	else:
		print("INCORRECT")

if __name__ == '__main__':
	# python is_bst.py < tests/3
	prev_value = -float("inf")
	threading.Thread(target=main).start()
