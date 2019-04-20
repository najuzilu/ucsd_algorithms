#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

'''
(2)is_bst_hard: use recursive method to determine each node whether it fits the requirement of a binary search tree. The trick is to write a function that traverses down the tree keeping track of the narrowing min and max allowed values as it goes, looking at each node only once.
function isBST(node, min, max){
    ...
    #If the node violate the max/min contraint, it's not a BST
    if (node <= min or node > max){
        return False
    }
    ...
    #For the left child, its maximum is root node
    #For the right child, its minimum is root node
    return isBST(leftnode, min, node) && isBST(rightnode, node, max)
    ...
}
'''

def IsBinarySearchTree(tree):
	if len(tree) < 1:
		return True
	root = tree[0]
	isBst(root, 0, 0)

def isBst(node, min_value, max_value):
	print(node[0], node[1], node[2], min_value, max_value)
	if (node[0] <= min_value) or (node[0] > max_value):
		return False
	return isBst(node[1], min_value, node[0]) and isBST(node[2], node[0], max_value)


def main():
	nodes = int(sys.stdin.readline().strip())
	tree = []
	for i in range(nodes):
		tree.append(list(map(int, sys.stdin.readline().strip().split())))
	
	IsBinarySearchTree(tree)
	# if IsBinarySearchTree(tree):
	# 	print("CORRECT")
	# else:
	# 	print("INCORRECT")

if __name__ == '__main__':
	# python is_bst_hard.py < tests/3
	min_value = -float("inf")
	max_value = float("inf")
	threading.Thread(target=main).start()
