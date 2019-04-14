## Why Study Algorithms ##

Which of the following is most representative of the types of algorithm problem we will focus on this class?  
**Answer**: Find the median of a list of numbers.

#### Coming up ####

Cover two algorithm problems:
* Fibonacci Numbers
* Greatest Common Divisors

## Fibonacci Numbers ##

What do you think the Fibonacci numbers were originally created to model?  
**Answer**: Rabbit populations

F_n >= 2^(n/2) for n >= 6  
**Proof**:  
By induction  
Base case: n = 6, 7 (by direct computation)
Inductive step:  
`F_n = F_(n-1) + F_(n-2) >= 2^((n-1)/2) + 2^((n-2)/2) >= 2 * 2^((n-2)/2) = 2^(n/2)`

**Theorem**:  
`F_n = (1/sqrt(5)) * ( ( (1 + sqrt(5)) / 2)^n - ( (1-sqrt(5)) / 2)^n )`

How do you compute Fibonacci numbers?

```
FibRecurs(n):
	if n <= 1:
		return n
	else:
		return FibRecurs(n-1) + FibRevurs(n-2)
```

How many digits do you think T(100) has?  
**Answer**: 20-30

#### Efficient Algorithm ####

Imitate hand computation:
0, 1, 1, 2, 3, 5, 8, ...

0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8

```
FibList(n):
	create an array F[0...n]
	F[0] <- 0
	F[1] <- 1
	for i from 2 to n:
		F[i] <- F[i-1] + F[i-2]
	return F[n]
```
T(n) = 2 * n + 2. So, T(100) = 202

## Greatest Common Divisor ##

* Put fraction a/b in simplest form
* Divide numerator and denominator by d, to get (a/d)/(b/d)
	* Need d to divide a and b
	* Want d to be as large as possible

**Definition**:  
For integers, a and b, their greatest common divisor or gcd(a, b) is the largest integer d so that d divides both a and b

What is the GCD(10, 4)?  
**Answer**: 2

```
Function NaiveGCD(a, b):
	best <- 0
	for d from 1 to (a + b):
	if d/a and d/b:
		best <- d
	return best
```
Runtime at most a+b

#### Efficient Algorithm ####

**Lemma**:  
Let a' be the remainder when a is divided by b, then  
gcd(a, b) = gcd(a', b) = gcd(b, a')

**Proof** (sketch):  
* a = a' + bq for some q
* d divides a and b if and only if it divides a' and b

```
Function EuclidGCD(a, b):
if b = 0:
	return a
a' <- the remainder when a is divided by b
return EuclidGCD(b, a')
```

What is GCD(357,234)? (You might want to use the Euclidean Algorithm)  
**Answer**: 3

## Big-O Notation ##

We want to:
* Measure runtime without knowing details how the program works, how the computer works
* Get results that work for large inputs

Idea:  
All of these issues can multiply runtimes by (large) constant.

Consider **asymptotic** runtimes. How does runtime **scale** with input size?

Runtimes:  
`log n` < `sqrt(n)` < `n` < `n log n` < `n^2` < `2^n`

**Definition of Big-O Notation**:  
f(n) = O( g(n) ) (f is Big-O of g) or f <= g if there exist constants N and c so that for all n >= N, f(n) <= c * g(n)

_Big-O is only asymptotic_

**Common Rules**:  
* `n^a < n^b` for 0 < a < b:
	* `n = O(n^2), sqrt(n) = O(n)`
* `n^a < b^n` (a > 0, b > 1):
	* `n^5 = O(sqrt(2)^n), n^100 = O(1.1^n)`
* `(log n)^a < n^b` (a, b > 0):
	* `(log n)^3 = O(sqrt(n)), n log n = O(n^2)`

**Other notations**:  
For functions f, g. N -> R we say that:
* `f(n) = $\Gamma$ (g(n)) or f >= g if for some c, f(n) >= c * g(n)` (f grows no slower than g)
* `f(n) = $\Theta$ (g(n)) or f ~ g if f = O(g) and f = $\Gamma$ (g)` (f grows at the same rate as g)

## Course Overview ##

Three most common algorithmic design techniques:
* Greedy Algorithms
* Divide and Conquer
* Dynamic Programming

Levels of Design:
* Naive Algorithm: definition to algorithm. Slow!
* Algorithm by way of standard tools: standard techniques
* Optimized Algorithm: improve existing algorithm
* Magic algorithm: unique insight