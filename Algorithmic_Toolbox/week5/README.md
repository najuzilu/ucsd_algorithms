## Advanced Reading ##
Chapter 5 "How Do We Compare Biological Sequences" of [CP]

[Advanced dynamic programming lecture notes](http://jeffe.cs.illinois.edu/teaching/algorithms/notes/D-faster-dynprog.pdf) by Jeff Erickson

Both sources explain, in particular, Hirschber's algorithm that allows to compute an optimal alignment (but not just its score!) of two strings of length n and mm in quadratic time O(nm)and a linear space O(m+n) only.

**References**:
* [DPV] Sanjoy Dasgupta, Christos Papadimitriou, and Umesh Vazirani. Algorithms (1st Edition). McGraw-Hill Higher Education. 2008.
* [CP] Phillip Compeau, Pavel Pevzner. Bioinformatics Algorithms: An Active Learning Approach. Active Learning Publishers. 2014.

Dynamic programming is probably the hardest part of the course. At the same time, it is definitely one of the most important algorithmic techniques. Please see additional slides (dynprog.pdf) that discuss an alternative perspective for dynamic programming algorithms: to get to a dynamic programming solution, we start from the most naive brute force solution and then start optimizing it. The slides also contain many pieces of Python code.