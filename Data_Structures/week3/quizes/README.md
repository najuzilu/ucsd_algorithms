## Priority Queues Quiz ##

1. How many edges of this binary tree violate the min-heap property? In other words, for how many edges of the tree, the parent value is greater than the value of the child?  
**Answer**: 4

2. This binary tree contains 13 nodes, and hence we have 13 subtrees here (rooted at each of 13 nodes). How many of them are complete?  
**Answer**: 11

3. Consider a complete binary tree represented by an array [19,14,28,15,16,7,27,15,21,21,5,2][19,14,28,15,16,7,27,15,21,21,5,2].

How many edges of this tree violate the max-heap property? In other words, for how many edges of the tree, the parent value is smaller than the value of the child?  
**Answer**: 5

4. Assume that a max-heap with 10^5 elements is stored in a complete 5-ary tree. Approximately how many comparisons a call to 𝙸𝚗𝚜𝚎𝚛𝚝() will make?  
**Answer**: 8

5. Assume that a max-heap with 10^6 elements is stored in a complete 7-ary tree. Approximately how many comparisons a call to 𝙴𝚡𝚝𝚛𝚊𝚌𝚝𝙼𝚊𝚡() will make?  
**Answer**: 50

6. Assume that we represent a complete dd-ary tree in an array A[1\dots n]A[1…n] -this is a 1-based array of size n. What is the right formula for the indices of children of a node number i?  
**Answer**: {(i-1)d+2, ..., min{n, (i-1)d+d+1}}

## Disjoint Sets Quiz ##

1. Consider the following program:
```
for i from 1 to 12:
  MakeSet(i)
Union(2, 10)
Union(7, 5)
Union(6, 1)
Union(3, 4)
Union(5, 11)
Union(7, 8)
Union(7, 3)
Union(12, 2)
Union(9, 6)
print(Find(6))
print(Find(3))
print(Find(11))
print(Find(9))
```
Assume that the disjoint sets data structure is implemented as an array 𝚜𝚖𝚊𝚕𝚕𝚎𝚜𝚝[1…12]: 𝚜𝚖𝚊𝚕𝚕𝚎𝚜𝚝[i] is equal to the smallest element in the set containing i.

What is the output of the following program? As an answer, enter four integers separated by spaces.  
**Answer**: 1 3 3 1

2. Consider the following program:
```
for i from 1 to 12:
  MakeSet(i)
Union(2, 10)
Union(7, 5)
Union(6, 1)
Union(3, 4)
Union(5, 11)
Union(7, 8)
Union(7, 3)
Union(12, 2)
Union(9, 6)
```
Assume that the disjoint sets data structure is implemented as disjoint trees with union by rank heuristic.

Compute the product of the heights of the resulting trees after executing the code. For example, for a forest consisting of four trees of height 1, 2, 3, 1 the answer would be 6. (Recall that the height of a tree is the number of edges on a longest path from the root to a leaf. In particular, the height of a tree consisting of just one node is equal to 0.)  
**Answer**: 2

3. Consider the following program:
```
for i from 1 to n:
  MakeSet(i)
for i from 1 to n-1:
  Union(i, i+1)
```
Assume that the disjoint sets data structure is implemented as disjoint trees with union by rank heuristic.

What is the number of trees in the forest and the maximum height of a tree in this forest after executing this code? (Recall that the height of a tree is the number of edges on a longest path from the root to a leaf. In particular, the height of a tree consisting of just one node is equal to 0.)  
**Answer**: One tree of height 1.

4. Consider the following program:
```
for i from 1 to 60:
  MakeSet(i)
for i from 1 to 30:
  Union(i, 2*i)
for i from 1 to 20:
  Union(i, 3*i)
for i from 1 to 12:
  Union(i, 5*i)
for i from 1 to 60:
  Find(i)
```
Assume that the disjoint sets data structure is implemented as disjoint trees with union by rank heuristic and with path compression heuristic.

Compute the maximum height of a tree in the resulting forest. (Recall that the height of a tree is the number of edges on a longest path from the root to a leaf. In particular, the height of a tree consisting of just one node is equal to 0.)  
**Answer**: 1

## Practice Quiz ##

1. You know from the lectures that a heap can be built from an array of nn integers in O(n) time. Heap is ordered such that each parent node has a key that is bigger than both children's keys. So it seems like we can sort an array of nn arbitrary integers in O(n) time by building a heap from it. Is it true?  
**Answer**: No 

2. You've organized a party, and your new robot is going to meet and greet the guests. However, you need to program your robot to specify in which order to greet the guests. Of course, guests who came earlier should be greeted before those who came later. If several guests came at the same time or together, however, you want to greet first the older guests to show them your respect. You want to use a min-heap in the program to determine which guest to greet next. What should be the comparison operator of the min-heap in this case?
**Answer**: 
```python
def GreetBefore(A, B):
  if A.arrival_time != B.arrival_time:
    return A.arrival_time < B.arrival_time
  return A.age > B.age
  ```

3. You want to implement a Disjoint Set Union data structure using both path compression and rank heuristics. You also want to store the size of each set to retrieve it in O(1). To do this, you've already created a class to store the nodes of DSU and implemented the FindFind method using the path compression heuristic. You now need to implement the UnionUnion method which will both use rank heuristics and update the size of the set. Which one is the correct implementation?  
**Answer**: 
```python
def Union(a, b):
  pa = Find(a)
  pb = Find(b)
  if pa.rank <= pb.rank:
    pa.parent = pb
    pb.size += pa.size
    if pa.rank == pb.rank:
      pb.rank += 1
  else:
    pb.parent = pa
    pa.size += pb.size
```