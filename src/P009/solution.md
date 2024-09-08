# Special Pythagorean triplet
There are a couple of ways of solving this.

## Compute $b$ and $c$ from $a$
Given:
$$a + b + c = 1000$$

Reordering and squaring that, we get:
$$c^2 = (1000 - a - b)^2$$

and given:
$$a^2 + b^2 = c^2$$

We get:
$$a^2 + b^2 = 1000^2 + a^2 + b^2 - 2000a - 2000b + 2ab$$

Simplifying that, we get:
$$b = 1000 * (500 - a) / (1000 - a)$$

Also, since: $a < b < c$ and $a + b + c = 1000$, we can see that $a < 333$.

Now simply iterate over all values of $a$.

## Use Euclid's formula
Euclid's formula states that a Pythagorean triple is formed by integers:

$$a = m^2 - n^2$$
$$b = 2mn$$
$$c = m^2 + n^2$$

where $m > n > 0$

Given:
$$a + b + c = 1000$$

We can write that in terms of $m$ and $n$ as,
$$2m^2 + 2mn = 1000$$

Or,
$$m * (m + n) = 500$$

Since $n > 0$, therefore $m < 22$

Now, go through all possible values of $m$ and $n$.

Finally,

$$
abc = (m^2 - n^2) \times 2mn \times (m^2 + n^2) = 2mn(m^4 - n^4)
$$
