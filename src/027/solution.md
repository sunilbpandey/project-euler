# Quadratic primes
Given,

$$
n^2 + an + b, \text{where}\ |a| < 1000\ \text{and}\ |b| \leq 1000\\
$$

If $n = 0$, the formula reduces to $b$. Since the result must be prime, this means $b$ must be a prime number.

If $n = b$, the formula yields $b^2 + ab + b$, which is clearly divisible by $b$. Therefore, $0 \leq n \lt b$. This means for any value of $a$ and $b$, the formula will never generate more than $b$ prime numbers. And since we are looking for a formula that will produce more than 40 primes, $b$ must be an odd prime number > 41.

If $n = 1$, the formula yields $1 + a + b$. For this to be a prime number, $a = 1 - b$ or $a$ must be odd.

If $n = 3$ and $a = 1 - b$, the formula yields $12 - 2b$, which is negative for any $b \ge 7$. Since we are looking for $b > 41$, $a$ must be odd.

Given the limits on $a$ and $b$ this formula cannot yield a number larger than 2,001,000. This is the largest number we need to test for primality. To do this efficiently, we can pre-compute prime numbers up to 1415.