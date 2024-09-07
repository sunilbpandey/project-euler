# Large sum
The key insight here is that we don't need to consider all the digits of the input numbers.

Since we are adding 100 numbers, adding the first 11 digits of each number will yield a 13-digit sum. The 12th digit of any input number can, at maximum, affect the 11th digit of the sum.

This means we need to consider only the first 11 digits, which should fit within the integer limit in most languages.
