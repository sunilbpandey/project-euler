# Reciprocal cycles
A brute force solution for this problem is to perform the division and compare remainders at each step until we find a cycle. This runs very fast, but we can apply some math to simplify this even further.

If d is a natural number coprime to 2 and 5, then the decimal expansion of 1/d has a period k such that k is the smallest number satisfying

$$
10^k \equiv 1 \mod d
$$

If d is not coprime to 2 or 5, say,

$$
d = 2^a5^bd_1
$$

where $d_1$ is coprime to 2 and 5, then the decimal expansion of 1/d will have the same period as 1/$d_1$.

Combining these two, we get that:

* We only need to check numbers that coprime to 2 and 5, and
* For those numbers, we can find the period by calculating powers of 10 until we find the appropriate k.
