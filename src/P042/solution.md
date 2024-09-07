# Coded triangle numbers
For a given number, $n$, to be a triangle number,

$$
n = \frac{k(k + 1)}{2}
$$

where $k$ is a natural number.

Multiplying both sides by 8 and adding 1, we get,

$$
8n + 1 = 4k(k + 1) + 1 = (2k + 1)^2
$$

Therefore, for $n$ to be a triangle number, $8n + 1$ must be a perfect square.

Another way of deriving the same result,

$$
n = \frac{k(k + 1)}{2}
$$

so,
$$
k^2 + k - 2n = 0
$$

Using the formula for the roots of a quadratic equation, we get,

$$
k = \frac{-1 \pm \sqrt{1 + 8n}}{2}
$$

Since $k$ is a natural number, $8n + 1$ must be a perfect square.
