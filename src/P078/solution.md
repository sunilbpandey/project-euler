# Coin Partitions
This problem is similar to problem [76](/src/076) (and also [31](/src/031) and [77](/src/077)), but that approach is very slow for this problem. Instead, a more efficient approach is to use the recurrence relation:

$$
P(n) = \sum_{k=1}^{n}(-1)^{k-1}[P(n - \frac{1}{2}k(3k - 1)) + P(n - \frac{1}{2}k(3k + 1))]
$$

The terms $\frac{1}{2}k(3k - 1)$ and $\frac{1}{2}k(3k + 1)$ are [generalized pentagonal numbers](https://mathworld.wolfram.com/PentagonalNumber.html).

Since $P(n) = 0$ when $n$ is negative, we can stop the recurrence as soon as one of these terms exceeds $n$.

We can also pre-compute these terms to avoid recalculating for every $n$.

Let,

$$
g_k = \frac{1}{2}k(3k - 1)
$$

The next term,

$$
g_{k + 1} = \frac{1}{2}(k + 1)(3k + 3 - 1)
$$

Simplifying, we get,

$$
g_{k + 1} = g_k + 3k + 1
$$

Or,

$$
g_k = g_{k - 1} + 3k - 2
$$

Similarly, for the second term $\frac{1}{2}k(3k + 1)$, we can see that,

$$
g_k = g_{k - 1} + 3k - 1
$$

## References
[Weisstein, Eric W.](https://mathworld.wolfram.com/about/author.html) "Partition Function P." From [MathWorld](https://mathworld.wolfram.com/)--A Wolfram Web Resource. https://mathworld.wolfram.com/PartitionFunctionP.html

[Weisstein, Eric W.](https://mathworld.wolfram.com/about/author.html) "Pentagonal Number." From [MathWorld](https://mathworld.wolfram.com/)--A Wolfram Web Resource. https://mathworld.wolfram.com/PentagonalNumber.html

[Pentagonal number theorem - Wikipedia](https://en.wikipedia.org/wiki/Pentagonal_number_theorem)

[Partition function (number theory) - Wikipedia](https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations)
