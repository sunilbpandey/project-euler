# Pandigital prime
The sum of digits from 1 to 9 is 45. Since 45 is divisible by 3, it follows that any 9-digit pandigital number is divisible by 3, and therefore not prime.

Similarly, any 8, 6, 5, 3 or 2 digit pandigital number is divisible by 3 and therefore not prime.

So, the answer must be a 7-digit or 4-digit pandigital number.

Let's assume 7-digit pandigital prime number exists. The largest such number is 7654321. $2767^2 = 7656289$. Therefore, if we pre-compute primes up to 2767, we can quickly test all 7-digit pandigital numbers.
