# Pandigital multiples
We are looking for a multiplier, m, such that the concatenated product of m with 1, 2, ..., n will generate a 1 to 9 pandigital number.

Since n > 1, and the concatenated product cannot have more than nine digits, we can see that m cannot have five or more digits.

We are given that m = 9 generates the concatenated product 918273645, and we are looking for a number larger than this. Since the first multiplicand is 1, we can see that m must start with 9. Also, clearly m must have two or more digits.

If m has two digits, we can observe that the concatenated product will have 8 digits (if n is 3) or 11 digits (if n is 4). So m cannot have two digits.

Simiarly, if m has three digits, the concatenated product will have 7 digits (if n is 2) or 11 digits(if n is 4). So m cannot have three digits either.

This gives us $999 < m < 10000$ and $n = 2$.
