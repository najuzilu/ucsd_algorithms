## Hash Tables and Hash Functions Quiz ##

1. What is the size of the array needed to store integer keys with up to 1212 digits using direct addressing?  
**Answer**: 10^12

2. What is the maximum possible chain length for a hash function h(x) = x mod 1000 used with a hash table of size 1000 for a universe of all integers with at most 12 digits?  
**Answer**: 10^9

3. You want to hash integers from 0 up to 1000000. What can be a good choice of p for the universal family?  
**Answer**: 1000003

4. How can one build a universal family of hash functions for integers between −1000000 (minus one million) and 1000000 (one million)?  
**Answer**: First, add 1000000 to each integer and get the range of integers between 0 and 2000000. Then use the universal family for integers with p = 2000003.