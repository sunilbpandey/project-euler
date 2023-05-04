# Totient maximum
## Brute force
The totient function can be calculated using the formula,

$$
\phi(n) = n(1 - \frac{1}{p_1})(1 - \frac{1}{p_2})\dots(1 - \frac{1}{p_r})
$$

where $p_1, p_2, \dots, p_r$ are all primes dividing $n$.

Using this formula we can calculate $n/\phi(n)$ for all values of $n$ between 2 and 1000000, and find the maximum.

## Faster approach
While the brute force approach works, we can do better.

Let's consider $n/\phi(n)$.

$$
\frac{n}{\phi(n)} = (\frac{p_1}{p_1 - 1})(\frac{p_2}{p_2 - 1})\dots(\frac{p_r}{p_r - 1})
$$

As we can see, this value depends only on the prime numbers that divide $n$, not on $n$ itself or even on the exponent of the prime numbers in the prime factorization of $n$.

The value $\frac{p}{p - 1}$ is the largest for the smallest prime number, 2, and gradually gets smaller, and closer to 1, for larger prime numbers. But it can never be less than 1.

If two numbers $n_1$ and $n_2$ have the same the prime factors, $n_1/\phi(n_1)$ and $n_2/\phi(n_2)$ will be equal.

If all the prime factors of $n_1$ also divide $n_2$, and $n_2$ has some additional prime factors, then $n_2/\phi(n_2)$ will be greater than $n_1/\phi(n_1)$.

If $n_1$ and $n_2$ have the same number of prime factors, $n/\phi(n)$ will be greater for whichever number has the numerically lower prime factors.

Putting all of that together, the product of as many smallest prime numbers as possible will have the maximum value of $n/\phi(n)$.

At this point, we can actually calculate the answer by hand: $2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 = 510510$. Multiplying any larger prime number will make the product be greater than 1000000, so 510510 is the answer!
