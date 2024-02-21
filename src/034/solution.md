# Digit factorials
This problem is similar to [problem 30](/src/030), and we can use the same approach to solve it, except that instead of fifth powers, we need to calculate factorials. Just like in problem 30, the order of digits doesn't matter, we just need to find sets of digits such that the sum of their factorials contains the same digits.

Now, consider the largest eight-digit number, 99999999. 8 * 9! = 2903040, which has only seven digits. So the sum of factorials of eight digits can never produce an eight-digit number. And since every subsequent digit can only add 362880 to the sum, no number of more than seven digits can be equal to the sum of the factorial of its digits.

Therefore, we have an upper bound of seven digits. Also, since we are looking for sums, the number must have at least two digits.
