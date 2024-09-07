# Triangular, pentagonal, and hexagonal
The formula for pentagonal numbers is,

$$
P_n = \frac{n(3n − 1)}{2}
$$

which gives us,

$$
24P_n + 1 = 36n^2 - 12n + 1 = (6n - 1)^2
$$

In other words, for a number, $p$, to be pentagonal, $24p + 1$ must be a perfect square.

The formula for hexagonal numbers is,

$$
H_n = n(2n − 1)
$$

which gives us,

$$
8H_n + 1 = 16n^2 - 8n + 1 = (4n - 1)^2
$$

In other words, for a number, $h$, to be hexagonal, $8h + 1$ must be a perfect square.

So we can generate triangular numbers and use these two tests to check if the number is also pentagonal and hexagonal.

However, we can do one small optimization.

Consider the triangle number,

$$
T_{2n - 1} = \frac{(2n - 1)(2n)}{2} = n(2n - 1) = H_n
$$

So, every hexagonal number is also a triangle number. This means if we just generate pentagonal numbers and test if the number is also hexagonal, we can get the answer without having to test if the number is triangular.
