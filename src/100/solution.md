# Arranged Probability

Let $B$ and $R$ be the number of blue and red discs, respectively. Then, the probability of taking two blue discs at random is,

$$
\frac{B}{B+R} \times \frac{B - 1}{B + R - 1}
$$

For this value to be $\frac{1}{2}$, we must have,

$$
2B(B - 1) = (B + R)(B + R - 1)
$$

Or,

$$
B^2 - (1 + 2R)B - R^2 + R = 0
$$

Solving for $B$,

$$
B = \frac{1 + 2R \pm \sqrt{(1 + 2R)^2 + 4R^2 - 4R}}{2} = \frac{1 + 2R \pm \sqrt{1 + 8R^2}}{2}
$$

Since $\sqrt{1 + 8R^2} \gt 2R$, one of the roots will be negative and can be ignored.

So,

$$
B = \frac{1 + 2R + \sqrt{1 + 8R^2}}{2}
$$

Now, for $B$ to be a natural number, $1 + 8R^2$ must be a square. In other words,

$$
1 + 8R^2 = m^2
$$

This gives us a [Pell's equation](https://en.wikipedia.org/wiki/Pell%27s_equation),

$$
m^2 - 8R^2 = 1
$$

The fundamental solution for this equation can be calculated as $m = 3$ and $R = 1$.

Further solutions can be calculated as,

$$
m_{k+1} = 3m_k + 8R_k\\
R_{k+1} = 3R_k + m_k
$$

Once $m$ and $R$ are known, $B$ can be calculated as,

$$
B = R + \frac{m + 1}{2}
$$

Starting with $m = 3$ and $R = 1$, compute successive values of $m$, $R$ and $B$ until the sum $B + R$ exceeds $10^{12}$.


## Alternative approach

Given the equations to find the additional solutions,

$$
m_{k+1} = 3m_k + 8R_k\\
R_{k+1} = 3R_k + m_k
$$

We can see that,

$$
R_{k+1} = 3R_k + 3m_{k-1} + 8R_{k-1} = 3R_k + 3(3R_{k-1} + m_{k-1}) - R_{k-1}
$$

Or,

$$
R_{k+1} = 6R_k - R_{k-1}
$$

Similarly, we can see that,

$$
m_{k+1} = 3m_k + 8R_k = 3R_{k+1} - 9R_k + 8R_k = 3R_{k+1} - R_k
$$

Also,

$$
B_k = R_k + \frac{m_k + 1}{2}
$$

Substituting the terms and simplifying, we get,

$$
B_k = \frac{R_{k+1} - R_k + 1}{2}
$$

Once again, compute successive values of $R$ and $B$ until the sum $B + R$ exceeds $10^{12}$.
