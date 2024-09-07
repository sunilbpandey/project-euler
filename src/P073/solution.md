# Counting fractions in a range
## Counting numerators
Consider a fraction $n/d$ such that $1/3 \lt n/d \lt 1/2$.

This means,

$$
2n < d \iff 2n \le d - 1 \iff n \le \lfloor \frac{d - 1}{2} \rfloor
$$

and,

$$
3n > d \iff n > \lfloor \frac{d}{3} \rfloor
$$

Additionally, the fraction $n/d$ must be a reduced proper fraction, so $\text{GCD}(n, d) = 1$.

Using these equations, we can count the number possible values of $n$ for every value of $d \le 12000$.

## Farey sequence
[Farey sequence](https://en.wikipedia.org/wiki/Farey_sequence) of order $n$, $F_n$, is the sequence of reduced fractions between 0 and 1, with denominator $d \le n$, arranged in ascending order.

One of the properties of the Farey sequences is that if $0 \le \frac{a}{b} \lt \frac{c}{d} \le 1$ are neighbours in some Farey sequence, then the fraction between them with the smallest denominator is their [mediant](https://en.wikipedia.org/wiki/Mediant_(mathematics)) $\frac{a + c}{b + d}$.

Using this property, and starting with $\frac{1}{3}$ and $\frac{1}{2}$, we can generate all fractions between them.

Start with,

$$
\frac{1}{3}, \frac{1}{2}
$$

Add the numerators and denominators to get the next fraction,

$$
\frac{1}{3}, \frac{2}{5}, \frac{1}{2}
$$

Add the numerators and denominators of each pair of neighbours to get the fraction between them,

$$
\frac{1}{3}, \frac{3}{8}, \frac{2}{5}, \frac{3}{7}, \frac{1}{2}
$$

and so on.

For this problem, we don't need to consider numerators. So the expansion proceeds as,

$$
3, 2
$$

Then,

$$
3, 5, 2
$$

Then,

$$
3, 8, 5, 7, 2
$$

and so on. If a new value would exceed 12000, don't add it to the sequence. We can stop when no new values are added to the sequence.

An efficient way of implementing this is using depth-first traversal. See also: [Stern-Brocot tree](https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree).

Start with 3 and 2. Then next number is 3 + 2 = 5. Now look for the number between 3 and 5, which is 8. Now look for the number between 3 and 8, which is 11, and so on until the mediant exceeds 12000.

This can be implemented using recursion, or for better performance, using a stack.
