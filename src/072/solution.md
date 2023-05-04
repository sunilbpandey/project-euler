# Counting fractions
## Using Euler's totient function
Consider all the fractions, $n/d$, for a given denominator, $d$. Since $n \lt d$ and $\text{GCD}(n, d) = 1$, this means $n$ and $d$ must be co-prime. So, to count the number of reduced proper fractions with denominator $d$, we just need to know the count of numbers smaller than $d$ that are coprime to $d$. This number is given by Euler's [totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function).

The totient function, $\phi(n)$, for any number $n$, can be calculated from its prime factors,

$$
\phi(n) = n(1 - \frac{1}{p_1})(1 - \frac{1}{p_2})\dots(1 - \frac{1}{p_r})
$$

where $p_1, p_2, \dots, p_r$ are all primes dividing $n$.

So the answer we are looking for is $\sum_{n=2}^{1000000}\phi(n)$.

## Optimizing the calculation of $\phi(n)$
Calculating $\phi(n)$ for every number takes time. But we can optimize it by avoiding division.

Consider a number, $n$, with prime factors $p_1, p_2, \dots, p_r$,

$$
n = \prod_{i=0}^rp_i^{a_i}
$$

and,

$$
\phi(n) = n\prod_{i=0}^r(p_i - 1)p_i^{-1}
$$

Combining the two,

$$
\phi(n) = \prod_{i=0}^r(p_i - 1)p_i^{a_i-1}
$$

Take one of the prime numbers dividing $n$,

$$
n = m \times p_k
$$

If $p_k$ does not divide $m$,

$$
\phi(m) = m\prod_{i \ne k}p_i
$$

which gives us,

$$
\phi(n) = \phi(m) \times p_k \times \frac{p_k - 1}{p_k} = \phi(m) \times (p_k - 1)
$$

If $p_k$ divides $m$,

$$
\phi(m) = m\prod_{i=0}^r(p_i - 1)p_i^{-1}
$$

which gives us,

$$
\phi(n) = \phi(m) \times p_k
$$

So, if we have already calculated $\phi(m)$ for the smaller number, $m$, we can calculate $\phi(n)$ more efficiently.

We can use a sieve method. Initialize an array, arr, of size N to all zeroes. Also create an array of prime numbers, initially empty. Now go through the array values starting at index 2,

- If the array value at current index, i, is 0, that means i is a prime number
    - Add i it to the list of prime numbers
    - Set the arr[i] to i - 1
- For every prime number, p, found so far, update the array value for the product of p and i.
    - If p divides i, set arr[i * p] to arr[i] * p
    - If p does not divide i, set arr[i * p] to arr[i] * (p - 1)

Once the entire array has been traversed, arr[i] has $\phi(i)$ for all i > 1. The answer we are looking for is the sum of all array values for i > 1.
