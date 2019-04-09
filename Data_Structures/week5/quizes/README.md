## Binary Search Tress Quiz ##

1. Your colleague proposed a different definition of a binary search tree: it is such binary tree with keys in the nodes that for each node the key of its left child (if exists) is less than its key, and the key of its right child (if exists) is bigger than its key. Is this a good definition for a binary search tree?  
**Answer**: No
**Explanation**: Think of tree with root node 3 and childrem with node 1 and 4 where node 4 has chil 2.

2. Suppose we enforce the AVL tree condition only for the root of the tree, but not for all the nodes. Can such tree be unbalanced?  
**Answer**: Yes

3. Can the Insert operation be implemented given only Split and Merge operations?
**Answer**: Yes. First create a new tree with single key - the key to be inserted. Then split the current tree by this key. Then merge the left splitted part with the new tree. Then merge the result with the right splitted part.

4. Can the Delete operation be implemented given only Split and Merge operations?
**Answer**: Yes. Suppose we are deleting key x. Split by the key twice: one split such that all the keys < x go to the left and all the keys >= x go to the right. Then split the right part of the first split such that all the keys <= x go to the left and all the keys >x go to the right. Then merge the left part of the first split and the right part of the second split - thus leaving out the node with key x if there was such a node.