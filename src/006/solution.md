# Sum square difference

Since the problem is limited to only first 100 natural numbers, a brute force solution is fast enough. But the two sums can be computed more directly.

Sum of first $n$ natural numbers is given by this formula:

$$
\sum_{k=1}^nk = \frac{1}{2}n\left(n + 1\right)
$$

Sum of squares of first $n$ natural numbers is given by this formula:

$$
\sum_{k=1}^nk^2 = \frac{1}{6}n\left(n + 1\right)\left(2n + 1\right)
$$

Yet another approach is to consider the square of sums,

$$
(a + b \dots + n)^2 = (a^2 + b^2 + \dots + n^2) + (2ab + 2ac + \dots + 2an + 2bc + \dots + 2bn + \dots)
$$

So the difference between the sum of the squares and the square of the sum is,

$$
2 * (ab + ac + \dots + an + bc + \dots + bn + \dots)
$$

i.e. 2 multiplied by the sum of product of every pair of numbers in $a \dots n$.


## References
[Weisstein, Eric W.](https://mathworld.wolfram.com/about/author.html) "Power Sum." From *[MathWorld](https://mathworld.wolfram.com/)*--A Wolfram Web Resource. https://mathworld.wolfram.com/PowerSum.html
 
