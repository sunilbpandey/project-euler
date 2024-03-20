# Almost Equilateral Triangles

Given an isosceles triangle with two sides equal to $a$ and the third side $b = a \pm 1$, its area is given by,

$$
\frac{1}{2} \times b \times h
$$

where $h$ is the height of the triangle.

We can see that for the area to be an integer, $a$, $h$ and $\frac{b}{2}$ must form a Pythagorean triple.

[Euclid's formula](https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple) states that a Pythagorean triple is formed by integers:

$p = m^2 - n^2,\ q = 2mn,\ r = m^2 + n^2$

where $m > n > 0$

For the larger triangle to be almost equilateral, one of the following must be true:

$$
r = 2p \pm 1\\
r = 2q \pm 1
$$

Substituting $m$ and $n$, we get that one of the following must be true:

$$
m^2 = 3n^2 \pm 1\\
m^2 = n(4m - n) \pm 1
$$

Using the quadratic formula, we can calculate $m$ for a given $n$.

Since $m > n$, the possible values of $m$ for a given $n$ are,

$$
\sqrt{3n^2 \pm 1}\\
2n + \sqrt{3n^2 \pm 1}
$$

Also, the perimeter of the larger triangle is either $2(r + p)$ or $2(r + q)$, or either $4m^2$ or $2(m + n)^2$.

Given this perimeter should not exceed one billion, and since $m \gt n$, we get $0 \lt n \lt 15812$.

Now, go through all values of $n$ in this range, compute $m$ and see if the pair satisfies all the conditions.
