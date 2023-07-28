# Integer right triangles
As we did in [problem 9](src/009), there are a couple of ways of solving this problem.

## Compute $b$ and $c$ from $a$ and $p$
Given, $a + b + c = p$ and, $a^2 + b^2 = c^2$

we get,

$$
a^2 + b^2 = (p - a - b)^2 = p^2 + a^2 + b^2 - 2ap - 2bp + 2ab
$$

or,

$$
2b(a - p) = 2ap - p^2 = 2p(a - p) + p^2
$$

or,

$$
2(a - p)(b - p) = p^2
$$

which gives us,

$$
b = p + \frac{p^2}{2(a - p)}
$$

Since $b$ is an integer, $p^2$ must be divisible by $2(a - p)$. This also implies that $p$ must be even.

If $a = b$, $a^2 + b^2 = 2a^2 = c^2$. Since both $a$ and $c$ are integers, this is not possible. Therefore, $a \ne b$. Without loss of generality, let's assume $a < b$.

Finally, since $a + b > c$, otherwise the sides won't form a triangle, and $a + b + c = p$, so $p > 2c$. Since $p \le 1000$, this means $c < 500$. And because this is a right triangle, $c$ is the longest side, which means $a < 500$.

Now we can go through all values of $p$ and count the number of values of $a$ which produce a valid $b$.

## Use Euclid's formula
We can also use [Euclid's formula](https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple), which states that a Pythagorean triple is formed by integers:

$a = m^2 - n^2,\ b = 2mn,\ c = m^2 + n^2$

where $m > n > 0$

Given a perimeter, $p$,

$$
a + b + c = p
$$

gives us,

$$
2m(m + n) = p
$$

We can see that the perimeter must be even.

Also, since $p \le 1000$,

$$
m(m + n) \le 500
$$

Since $n > 0$, therefore $1 < m < 22$

The formula generates all primitive triples if $m$ and $n$ are coprime and at least one of them is even. However, it does not generate all triples. We can generate non-primitive triples by adding another parameter, $k$.

$a = k(m^2 - n^2),\ b = 2kmn,\ c = k(m^2 + n^2)$

Once we have generated a primitive triple, we can multiply each number with an increasing value of $k$ until the perimeter exceeds 1000.
