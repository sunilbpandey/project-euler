# Circular primes
Any number with two or more digits that ends in 0, 2, 4, 5, 6 or 8, is divisible by 2 or 5, and therefore not prime. So any prime number with two or more digits must end in 1, 3, 7 or 9.

Since we are looking at rotations of digits, every digit of the number must be one of 1, 3, 7 or 9. Now we just need to look for all permutations of these four digits, and check if all their rotations are prime numbers.

To efficiently check if a number below one million is prime, we can pre-compute prime numbers up to one thousand.
