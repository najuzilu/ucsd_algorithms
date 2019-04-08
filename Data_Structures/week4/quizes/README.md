## Hash Tables and Hash Functions Quiz ##

1. What is the size of the array needed to store integer keys with up to 1212 digits using direct addressing?  
**Answer**: 10^12

2. What is the maximum possible chain length for a hash function h(x) = x mod 1000 used with a hash table of size 1000 for a universe of all integers with at most 12 digits?  
**Answer**: 10^9

3. You want to hash integers from 0 up to 1000000. What can be a good choice of p for the universal family?  
**Answer**: 1000003

4. How can one build a universal family of hash functions for integers between −1000000 (minus one million) and 1000000 (one million)?  
**Answer**: First, add 1000000 to each integer and get the range of integers between 0 and 2000000. Then use the universal family for integers with p = 2000003.

## Practice Quiz: Hashing ##

1. What is the minimum size of an array that can be used in the direct addressing scheme to store a map from 7-digit phone numbers to names?  
**Answer**: 10^7

2. If it is guaranteed that the total length of all occurrences of a Pattern in a TextText is at most L, which of the below estimates of the average running time of Rabin-Karp's algorithm to find all occurrences of the Pattern in the Text is the most tight out of the correct ones?  
**Answer**: O(∣Text∣+∣Pattern∣+L)

3. Let us slightly change the polynomial hash function for strings and set `h(S)=(∑ [j=0,|S|−1] x^(|S|−1−j) * S[j]) mod p`. Let us fix some Text and some Pattern. Denote by H[i] the hash function of the substring Text[i..i+|Pattern|-1] of the Text starting from position i and having the same length as Pattern (for all appropriate positions i where the Pattern can occur in the Text). Which of the below formulas is the correct recurrence to compute H[i + 1] given H[i]?
**Answer**: `H[i+1]=(xH[i]+Text[i+|Pattern|]−x^(|Pattern|) * Text[i]) mod p`  
**Explanation**: When we move one position to the right from position i, each term must increase the power of x in it by one, the first term x^(|Pattern|) * Text[i] must be subtracted after that, and a new term Text[i + |Pattern|] must be added.