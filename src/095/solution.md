# Amicable Chains

Sum of proper divisors of a number, $n$, can be calculated in a number of ways. We can go through all numbers from $1$ to $n - 1$, adding up all the numbers that divide $n$. Or we can prime factorize $n$, and calculate the sum as,

$$
\prod_{i=1}^r\frac{p_i^{a_i + 1} - 1}{p_i - 1}
$$

where $p_1, p_2, \dots p_r$ are prime factors of $n$, and $a_1, a_2, \dots a_r$ are their corresponding exponents.

However, since we have to compute sum of divisors of all numbers from 2 to one million, the fastest method is to build it like the prime sieve.

First, create an array of length one million, and initialize it with all 1s since every number is divisible by 1.

Now, add 2 to every 2nd element starting at array index 4, because every 2nd number is divisible by 2. We start at 4 instead of 2 because we want the sum of proper divisors.

Continue like this, add 3 to every 3rd element starting at index 6, add 4 to every 4th element starting at index 8, and so on. Stop adding to an element whenever it exceeds one million.

Once the array is filled, we need to find the longest cycle. Starting at every array index, we can use the [tortoise and hare algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare) to find cycles. If any element in the cycle exceeds one million, skip this cycle and move to the next index.
