## Exact Pattern Matching Quiz ##

1. For the Brute Force algorithm (from this lecture) matching some Pattern against the Text AAAAAAAAAAT, which of the Patterns below will require the maximum number of comparisons throughout the whole algorithm?  
**Answer**: AAAA

2. You've just tried to match the Pattern AACTAACAT against some Text starting from position 3 and you know that AACTAAC is the longest common prefix of the Pattern and the suffix of the Text starting in position 3:
???𝙰𝙰𝙲𝚃𝙰𝙰𝙲?????????????  
   𝙰𝙰𝙲𝚃𝙰𝙰𝙲𝙰𝚃  
What is the maximum amount by which you can shift the Pattern to the right without missing an occurrence of the Pattern in the Text?  
**Answer**: 4

3. What are the values of the prefix function for the string ACATACATACACA?     
**Answer**: [0, 0, 1, 0, 1, 2, 3, 4, 5, 6, 7, 2, 3]

4. What is the total number of times that the condition of the while loop will be checked in this pseudocode for ComputePrefixFunction if we call it for the string ACATACATACACA?  
**Answer**: 12,13, 14, **answer**:15


