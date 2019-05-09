## Linear Search and Binary Search Quiz ##

1. You have an array with 1023 numbers. You use linear search to determine whether number 239 is in this array or not. How many elements of the array will you look at if number 239 is not present in the array?  
**Answer**: 1023

2. Can you use binary search to find number 8 in the array [1, 24, 25, 23, 17, 8, 9]?  
**Answer**: No

3. You have a sorted array with 1023 elements. You use binary search to determine whether number 239 is present in this array or not. How many elements of the array will you compare it with if number 239 is not present in this array?  
**Answer**: 10

4. What is the maximum number of iterations a binary search will make to find some number in the array [1, 2, 3, 5, 8, 13, 21, 34]?  
**Answer**: 4

## Polynomial Multiplication Quiz ##

1. For `n = 1024`, compute how many operations will the faster divide and conquer algorithm from the lectures perform, using the formula `3^(log base 2 of n)` for the number of operations.  
**Answer**: 

2. What is the key formula used in the faster divide and conquer algorithm to decrease the number of multiplications needed from 4 to 3?  
**Answer**: `a_1 b_0 + a_0 b_1 = (a_0 + a_1) (b_0 + b_1) - a_0 b_0 - a_1 b_1`

3. How to apply fast polynomial multiplication algorithm to multiply very big integer numbers (containing hundreds of thousands of digits) faster?  
**Answer**: For a number A = ...(_select long answer_)

## Master Theorem Quiz ##

1. Mark all the correct statements.  
**Answer**: 
* `If T(n)=T(n/2)+O(1) then T(n)=O(log n)`
* `If T(n)=8T(n/2)+O(n^2) then T(n)=O(n^4)`