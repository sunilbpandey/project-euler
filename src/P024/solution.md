# Lexicographic permutations
While a brute force solution, i.e. enumerating all the permutations until we find the millionth one, is fast enough, this can be solved a lot faster directly.

We are looking for permutations of 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. There are $n!$ permutations for $n$ digits, so the first $9!$ permutations in lexicographical order will start with 0, the next $9!$ will start with 1, and so on.

Observe that $9! * 2 = 725760$ is less than 1 million and $9! * 3 = 1088640$ is greater. So the first digit must be 2.

Find the number of permutations we still need to count:\
$999999 - 725760 = 274239$

So the problem now reduces to finding 274239th permutation of the remaining 9 digits: 0, 1, 3, 4, 5, 6, 7, 8, 9.

Applying the same method, we see that $8! * 6 = 241920$ is less than 274239 but $8! * 7 = 282240$ is greater. So the next digit must be the 6th digit, i.e. 7.

Continue in this manner until all the digits are found.
