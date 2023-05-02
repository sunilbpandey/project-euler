# Powerful digit counts
Say the number we are looking for has $n$ digits and is equal to $m^n$ for some $m$.

$10^n$ has n + 1 digits, so $0 \lt m \lt 10$.

Given this, we know that $m^1 = m$ will have exactly 1 digit.

As $n$ increases, $10^n$ will increase faster than $m^n$, so at some point $m^n$ will have fewer than $n$ digits. At this point,

$$
m^n < 10^{n - 1}
$$

If we increase $n$ further,

$$
m^{n + 1} = m \times m^n < m \times 10^{n - 1}
$$

But since $m < 10$,

$$
m^{n + 1} < 10 \times 10^{n - 1}
$$

Or,

$$
m^{n + 1} < 10^n
$$

This means once $m^n$ has fewer than $n$ digits, all higher values of $n$ will have fewer than $n$ digits.

At this point, we can go through all values of $m$ and $n$ until $m^n$ has fewer than $n$ digits, and count the number of times it has exactly $n$ digits.

## Direct computation using logarithm
We can take the mathematical analysis a step further and avoid calculating $m^n$ altogether.

Given $0 \lt m \lt 10$, we know that n = 1 works because $m^1 = m$ will have exactly one digit.

So we are looking for the largest value of $n$ such that,

$$
m^n \ge 10^{n - 1}
$$

Take logarithm base 10 of both sides,

$$
n \log_{10}(m) \ge n\log_{10}(10) - \log_{10}(10)
$$

Or,

$$
n \le \frac{1}{1 - log_{10}(m)}
$$
