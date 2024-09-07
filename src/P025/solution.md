# 1000-digit Fibonacci number
This can be easily solved with brute force. As with [problem 16](/src/016) and [problem 20](/src/020), the only complication is handling very large numbers, and the same approach that was used in those problems can be used here.

But, there is a simpler way to calculate this using the [golden ratio](https://mathworld.wolfram.com/GoldenRatio.html).

The nth Fibonacci number is,

$$
F_n = [ \frac{\phi^n}{\sqrt{5}} ]
$$

where $[x]$ is the nearest integer.

Since we want the number to have 1000 digits,

$$
F_n > 10^{999}\\
$$

Using the earlier formula and taking log of both sides, we get,

$$
n * log(\phi) - \frac{log(5)}{2} > 999 * log(10)
$$

which gives us,

$$
n  > \frac{999 * log(10) + \frac{log(5)}{2}}{log(\phi)}
$$

$n$ can now be calculated with a simple calculator.

## References
[Chandra, Pravin](https://mathworld.wolfram.com/topics/Chandra.html) and [Weisstein, Eric W.](https://mathworld.wolfram.com/about/author.html) "Fibonacci Number." From *[MathWorld](https://mathworld.wolfram.com/)*--A Wolfram Web Resource. https://mathworld.wolfram.com/FibonacciNumber.html

[Weisstein, Eric W.](https://mathworld.wolfram.com/about/author.html) "Golden Ratio." From *[MathWorld](https://mathworld.wolfram.com/)*--A Wolfram Web Resource. https://mathworld.wolfram.com/GoldenRatio.html
