# Singular Integer Right Triangles
This problem can be solved using the same approaches as [problem 9](/src/009) and [problem 39](/src/039).

## Use Euclid's formula
[Euclid's formula](https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple) states that a Pythagorean triple is formed by integers:

$a = m^2 - n^2,\ b = 2mn,\ c = m^2 + n^2$

where $m > n > 0$

Given a perimeter, $L$ = $a + b + c$

we get, $L = 2m(m + n) \le 1500000$

Since $n > 0$, this means $1 < m < 867$

The formula generates all primitive triples if $m$ and $n$ are coprime and at least one of them is even. However, it does not generate all triples. We can generate non-primitive triples by adding another parameter, $k$.

$a = k(m^2 - n^2),\ b = 2kmn,\ c = k(m^2 + n^2)$

Once we have generated a primitive triple, we can multiply each number with an increasing value of $k$ until the perimeter exceeds 1500000.
