# Amicable numbers
There are a couple of ways of solving this.

First approach is to find all the divisors of the number, $n$, and then sum up the proper divisors. One important optimization is to stop testing at the square root of $n$ instead of going all the way to $n$. If we know that $n$ is divisible by $d$, then we know that $n$ is also divisible by $n / d$. So if we include $d$ and $n/d$, we don't need to test any number greater than the square root of $n$.

Another approach is to use the prime factors of $n$. If $n$ is written in terms of its prime factors,

$$
n = p_1^{a_1} p_2^{a_2} \dots p_r^{a_r}
$$

Then the [sum of its divisors](https://mathworld.wolfram.com/DivisorFunction.html) can be calculated as,

$$
\sigma_1(n) = \prod^r_{i=1}\frac{p_i^{a_i+1} - 1}{p_i - 1}
$$

## References
[Weisstein, Eric W.](https://mathworld.wolfram.com/about/author.html) "Divisor Function." From *[MathWorld](https://mathworld.wolfram.com/)*--A Wolfram Web Resource. https://mathworld.wolfram.com/DivisorFunction.html
