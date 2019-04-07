## Dynamic Arrays and Amortized Analysis Quiz ##

1. Let's imagine we add support to our dynamic array for a new operation PopBack (which removes the last element), and that PopBack never reallocates the associated dynamically-allocated array. Calling PopBack on an empty dynamic array is an error.

If we have a sequence of 48 operations on an empty dynamic array: 24 PushBack and 24 PopBack (not necessarily in that order), we clearly end with a size of 0.

What are the minimum and maximum possible final capacities given such a sequence of 48 operations on an empty dynamic array? Assume that PushBack doubles the capacity, if necessary, as in lecture.  
**Answer**: minimum 1, maximum 32

2. Let's imagine we add support to our dynamic array for a new operation PopBack (which removes the last element). PopBack will reallocate the dynamically-allocated array if the size is \leq≤ the capacity / 2 to a new array of half the capacity. So, for example, if, before a PopBack the size were 5 and the capacity were 8, then after the PopBack, the size would be 4 and the capacity would be 4.

Give an example of nn operations starting from an empty array that require O(n^2) copies.  
**Answer**: Let n be a power of 2. Add n/2 elements, then alternate n/4 times between doing a PushBack of an element and a PopBack.

3. Let's imagine we add support to our dynamic array for a new operation PopBack (which removes the last element). Calling PopBack on an empty dynamic array is an error.

PopBack reallocates the dynamically-allocated array to a new array of half the capacity if the size is <= the capacity / 4 . So, for example, if, before a PopBack the size were 5 and the capacity were 8, then after the PopBack, the size would be 4 and the capacity would be 8. Only after two more PopBack when the size went down to 2 would the capacity go down to 4.

We want to consider the worst-case sequence of any nn PushBack and PopBack operations, starting with an empty dynamic array.

What potential function would work best to show an amortized O(1) cost per operation?  
**Answer**: theta(h) = max(2 * size - capacity, capacity / 2 - size)

4. Imagine a stack with a new operation: PopMany which takes a parameter, i, that specifies how many elements to pop from the stack. The cost of this operation is i, the number of elements that need to be popped.

Without this new operation, the amortized cost of any operation in a sequence of stack operations (Push, Pop, Top) is O(1) since the true cost of each operation is O(1).

What is the amortized cost of any operation in a sequence of nn stack operations (starting with an empty stack) that includes PopMany (choose the best answers)?  
**Answer**: 
* O(1) because we can define theta(h) = size
* O(1) because we can place one token on each item in the stack when it is pushed. That token will pay for popping it off with a PopMany
* O(1) because the sum of the costs of all PopMany operations in a total of n operations is O(n)
