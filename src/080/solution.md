# Square Root Digital Expansion
There are several methods for computing square roots which can be used to solve this problem, e.g. [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method#Square_root), [long division](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Decimal_(base_10)), etc. To avoid floating point precision errors when using Newton's method, multiply the number with $10^{200}$ before computing the square root.

But my favourite approach is one described by [Dr. Frazer Jarvis](https://www.sheffield.ac.uk/maths/people/academic/frazer-jarvis) in his 2005 paper "Square roots by subtraction". This is apparently an old Japanese method, and while it's slower than Newton's method, there is no division involved, so it avoids precision errors. And the algorithm is incredibly simple to implement!

To calculate the square root of $n$, let $a = 5n$ and $b = 5$.

Then repeatedly apply this step:

If $a \ge b$,

$$
a = a - b\\
b = b + 10
$$

Otherwise,

$$
a = 100a\\
b = 10b - 45
$$

The digits of $b$ will approach the digits of the square root of $n$.

Since we are interested in finding the first 100 digits, both $a$ and $b$ will get pretty large. If the language doesn't support arbitrarily large numbers, they can stored as strings or arrays.

## References
Jarvis AF (2005) Square roots by subtraction. Mathematical Spectrum, 37, 119-122
