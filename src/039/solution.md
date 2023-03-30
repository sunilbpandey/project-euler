# Integer right triangles
As we did in [problem 9](src/009), we can use [Euclid's formula](https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple), which states that a Pythagorean triple is formed by integers:

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
