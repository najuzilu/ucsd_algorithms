## Tries and Suffix Trees Practice Quiz ##

1. What is the tightest estimate you can prove on the memory consumption of a trie built off n non-empty patterns p1, p2,...,pn if all the patterns' lengths are bounded from above by L, and the sum of lengths of all patterns is no more than S?  
**Answer**: O(S)

2. What is the time complexity of searching all occurrences of n patterns p1, p2,...,pn in text T of length ∣T∣ if all patterns have length at most L and the sum of their lengths is at most S?  
**Answer**: O(∣T∣L)

3. What is the smallest possible number of nodes in a trie built off n patterns p1, p2,...,pn if all the patterns have the same length L>0?  
**Answer**: L + 1

4. If you take all the suffixes of a string S of length L and build a regular trie off those suffixes as patterns, what is the maximum possible number of nodes in such trie?  
**Answer**: ((L+1) * L) / 2 + 1

5. What is the smallest possible number of nodes in a suffix tree of string S with length L?  
**Answer**: L + 1