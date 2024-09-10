# Highly divisible triangular number

Consider a number $n$ written in terms of its prime factors:

$$
n = p_1^{a_1} p_2^{a_2} \dots
$$

Every divisor of $n$ must include zero or more of one or more of these prime numbers. So the total number of divisors of $n$ can be calculated as:

$$
d(n) = (a_1 + 1) (a_2 + 1) \dots
$$

Now, we can go through all the triangular numbers counting divisors until we find the answer, but that would require factorizing large numbers, which is inefficient and can be avoided.

The $n^{th}$ triangular number is the sum of first $n$ natural numbers. So the formula for triangular numbers is,

$$
T_n = \frac{n * (n + 1)}{2}
$$

If $n$ is even, let $n = 2k, \text{where } k > 0$. And if $n$ is odd, let $n = 2k -1, \text{where } k>0$. This gives,

$$
T_n =
\begin{cases}
k * (2k + 1) & \text{if } n \text{ is even}\\
k * (2k - 1) & \text{if } n \text{ is odd}
\end{cases}
$$

Let,

$$
d = GCD(k, 2k + 1)
$$

Therefore,

$$
k = p*d \quad \text{where } p > 0
$$

and,

$$
2k + 1 = q*d \quad \text{where } q > 0
$$

Combining the two, we get,

$$
d * (q - 2p) = 1
$$

Since d, p and q are all natural numbers, d must be 1. Therefore, k and (2k + 1) are [coprime](https://mathworld.wolfram.com/RelativelyPrime.html). Similarly, we can prove that k and (2k - 1) are coprime.

Finally, let $m$ and $n$ be two coprime natural numbers, written in terms of their prime factors as,

$$
m = p_1^{a_1} p_2^{a_2} \dots\\
n = q_1^{b_1} q_2^{b_2} \dots
$$

Since they share no common factors except 1, their product, $m * n$ can be written as,

$$
mn = p_1^{a_1} p_2^{a_2} \dots * q_1^{b_1} q_2^{b_2} \dots
$$

So the number of divisors of $m * n$ is,

$$
d(mn) = (a_1 + 1) (a_2 + 1) \dots (b_1 + 1) (b_2 + 1) \dots
$$

Or,

$$
d(mn) = d(m) * d(n)
$$

So,

$$
d(T_n) =
\begin{cases}
d(k) * d(2k + 1) & \text{if } n \text{ is even} \\
d(k) * d(2k - 1) & \text{if } n \text{ is odd}
\end{cases}
$$

This means instead of counting the divisors of $T_n$, we only need to count the divisors of much smallers numbers, k, 2k - 1 and 2k + 1.
