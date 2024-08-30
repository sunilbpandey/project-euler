# Largest palindrome product

There are multiple ways to solve this problem.

## Brute force

Simply multiply every pair of 3-digit numbers and find the largest product which is also a palindrome. On my computer, a TypeScript solution following this approach runs within a few hundred milliseconds, but it is very inefficient.

## Optimizing the search

Consider,

$$
999 \times 999 = 998001\\
901 \times 999 = 900099
$$

Let's assume we will be able to find the palindrome product within this range of roughly 100,000 numbers.

So the number we are looking for is likely 6-digit long, and starts with 9. Since it is a palindrome, the final digit must also be 9. This means that both the 3-digit numbers must be odd. Further, neither of them should end in `5`.

Finally, observe that:

$$
949 \times 949 = 900601
$$

This means that at least one of the two numbers must be 949 or greater. Now we just need to go through all possible values for the two numbers, calculate their product and test if it is a palindrome.

On my computer, a TypeScript solution runs in under 10ms. But we can try another approach which is equally fast.

## Eliminating the need for palindrome testing

As we did above, let's assume that the number we are looking for is 6-digit long. Since it is a palindrome, it can be written as,

$$
n = 100000a + 10000b + 1000c + 100c + 10b + a = 100001a + 10010b + 1100c
$$

where $0 < a \le 9$ and $0 \le b, c \le 9$

Further, as we did above, let's assume that the first and last digit, i.e. $a$, is 9. So if we iterate through all possible values of $b$ and $c$, and calculate $n$, we know that it's already a palindrome by construction.

The last thing we need to do is verify that $n$ is a product of two 3-digit numbers. Since we know that one of those two numbers must be 949 or greater, we just need to divide $n$ by all odd numbers from 949 to 999, and check if the quotient is also a 3-digit number.
