# Combinatoric selections
There are exactly ten ways of selecting three from five, 12345:

$$
123, 124, 125, 134, 135, 145, 234, 235, 245, \text{and } 345
$$

In combinatorics, we use the notation, ${5 \choose 3} = 10$.

In general, ${n \choose r} = \frac{n!}{r!(n - r)!}$, where $r \le n$, $n! = n \times (n - 1) \times \dots \times 3 \times 2 \times 1$, and $0! = 1$.

It is not until $n = 23$, that a value exceeds one-million: ${23 \choose 10} = 1144066$.

How many, not necessarily distinct, values of ${n \choose r}$ for $1 \le n \le 100$, are greater than one-million?

Source: https://projecteuler.net/problem=53
