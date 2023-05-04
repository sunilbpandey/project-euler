# Totient permutation
## Brute force
As discussed in [problem 69](src/069), we can calculate the totient function for all numbers, find the numbers where $\phi(n)$ is a permutation of $n$, and then minimize the value of $n/\phi(n)$. This approach works, but is very slow.

## Faster approach
Recall from problem 69 that,

$$
\frac{n}{\phi(n)} = (\frac{p_1}{p_1 - 1})(\frac{p_2}{p_2 - 1})\dots(\frac{p_r}{p_r - 1})
$$

Unlike problem 69, this time we are looking for the minimum value of $n/\phi(n)$. This value will be minimum when the number has as few prime factors as possible, and those prime numbers should be as large as possible.

For a prime number $p$,

$$
\phi(p) = p - 1
$$

But if $p$ is prime, then it must end in 1, 3, 7 or 9, and subtracting 1 will only change the last digit. This means that $p$ and $p - 1$ cannot have the same set of digits, so the answer must have at least two prime factors.

Let's assume that the answer has exactly two prime factors, $p_1$ and $p_2$, where $p_1 < p_2$.

For $n/\phi(n)$ to be minimum, both $p_1$ and $p_2$ should be as large as possible. Since $\lfloor \sqrt{10000000} \rfloor = 3162$, $p_1$ should be as close to 3162 as possible. Say we start the search at $p_1 > 2000$. This means $p_2 < 5000$. So if we generate prime numbers up to 5000 and search for all values of $p_1$ between 2000 and 3162, we should be able to find the answer.

Also, since $n = p_1 \times p_2$,

$$
\phi(n) = p_1p_2(\frac{p_1 - 1}{p_1})(\frac{p_2 - 1}{p_2}) = (p_1 - 1)(p_2 - 1)
$$
