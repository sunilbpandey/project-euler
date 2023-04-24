# Permuted multiples
Since we are looking for six permutations of the digits, the number must have three or more digits.

Also, since x and 6x should have the same number of digits, the most significant digit cannot be 2 or higher, so it must be 1. This means we are looking for a number like $1d_1d_2...$

Following the same logic, $d_1$ cannot be 7 or more.

Also note that 3x has the same digits as x, which means x must also be divisible by 3.

The first digit of 2x must be either 2 or 3. Similarly the first digit must be either 3 or 4 for 3x, either 4 or 5 for 4x, either 5 or 6 for 5x and either 6 or 7 for 6x.

Also the last digit must be either 0 or 5 for 5x.

Now we can simply examine all numbers using these rules until we find the answer.
