## Splay Trees Quiz ##

1. What is going to happen if you forget to splay the last accessed vertex in the implementation of Find in case the key was not found in the splay tree?
**Answer**: The tree will work too slow on some sequences of operations.

2. What will happen if you splay the node with the smallest key in a splay tree?
**Answer**: The root of the new tree won't have left child.

3. What will happen if you select a node N, splay its predecessor P (the node with the largest key smaller than the key of N), then splay the node N itself?
**Answer**: N will be the root, PP will be the left child of the root, PP won't have a right child.