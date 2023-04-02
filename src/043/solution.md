# Sub-string divisibility
A brute force solution for this problem is to generate all permutations of the ten digits and test for divisibility. While this is fast enough, it is wasteful as it requires testing all 10!, or 3628800, numbers.

A better approach is to test for divisibility while generating the numbers, starting from $d_1$. We know that $d_1$ cannot be 0. Similarly, we know that $d_4$ must be even, and $d_6$ must be either 0 or 5. By eliminating the invalid cases early, we can drastically cut down the number of numbers we need to test.
