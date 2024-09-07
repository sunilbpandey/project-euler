# Lattice paths
To get from the top left corner to the bottom right corner of an $n$ x $n$ grid, we need to take $n$ steps right and $n$ steps down. The order of these steps doesn't matter.

The number of ways of choosing the $n$ steps to the right is given by the [binomial coefficient](https://mathworld.wolfram.com/BinomialCoefficient.html) ${2n\choose n}$, and the remaining $n$ steps will be down. So the total number of routes is ${2n\choose n}$.

## References
[Weisstein, Eric W.](https://mathworld.wolfram.com/about/author.html) "Binomial Coefficient." From *[MathWorld](https://mathworld.wolfram.com/)*--A Wolfram Web Resource. https://mathworld.wolfram.com/BinomialCoefficient.html
