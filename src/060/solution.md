# Prime pair sets
Since the numbers are being concatenated, clearly 2 and 5 cannot belong to the set because any number with two or more digits and ending in 2 or 5 cannot be prime.

All primes greater than 3 are either 1 or 2 mod 3. If a prime number that is 1 mod 3 is concatenated to another prime number that is 2 mod 3, the resulting number will be divisible by 3, and therefore not prime. So we can divide all the prime numbers into two sets and test them separately. 3 should be part of both the sets.
