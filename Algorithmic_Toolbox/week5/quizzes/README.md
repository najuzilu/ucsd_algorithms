## Practice Quiz Money Change ##
1. What is the smallest amount of money for which greedy strategy fails with coin denominations of 1, 8 and 20?  
**Answer**: 24

2. What is the minimum number of coins needed to change 32 into coins with denominations 1, 8, 20?  
**Answer**: 4

3. What is the running time of the dynamic programming algorithm to change mm using nn different coin denominations?  
**Answer**: O(nm)

4. Is it possible to change 997 using coins with denominations 2, 4 and 8?  
**Answer**: No

## Practice Quiz Edit Distance ##

1. How many insertions are needed to make axybc from abc?  
**Answer**: 2

2. What is the edit distance between words bread and really?  
**Answer**: 4

3. What is the edit distance between bread and really if it is allowed to insert and delete symbols, but forbidden to replace symbols?  
**Answer**: 5. At least 5 actions are needed: b and d must be deleted, and then at least 3 new symbols must be inserted to increase the length from 3 to 6.

4. (This is an advanced problem)  
We want to compute not only the edit distance dd between two words, but also the number of ways to edit the first word to get the second word using the minimum number dd of edits. Two ways are considered different if there is such i, 1 <= i <= d that on the i-th step the edits in these ways are different.  
To solve this problem, in addition to computing array T with edit distances between prefixes of the first and second word, we compute array ways, such that ways[i,j] = the number of ways to edit the prefix of length i of the first word to get the prefix of length j of the second word using the minimum possible number of edits.

Which is the correct way to compute ways[i,j] based on the previously computed values?
**Answer**: 
```python
ways[i, j] = 0
if T[i, j] == T[i - 1, j] + 1:
  ways[i, j] += ways[i - 1, j]
if T[i, j] == T[i, j - 1] + 1:
  ways[i, j] += ways[i, j - 1]
if word1[i] == word2[j] and T[i, j] == T[i - 1, j - 1]:
  ways[i, j] += ways[i - 1, j - 1]
if T[i, j] == T[i - 1, j - 1] + 1:
  ways[i, j] += ways[i - 1, j - 1]
```