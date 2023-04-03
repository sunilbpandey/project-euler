# Sub-string divisibility
A brute force solution for this problem is to generate all permutations of the ten digits and test for divisibility. While this is fast enough, it is wasteful as it requires testing all 10!, or 3628800, numbers.

A better approach is to test for divisibility while generating the numbers, starting from $d_1$. We know that $d_1$ cannot be 0. Similarly, we know that $d_4$ must be even, and $d_6$ must be either 0 or 5. By eliminating the invalid cases early, we can drastically cut down the number of numbers we need to test.

## Solving using pen and paper
Incredibly, this can actually be solved manually. We know that $d_6$ must be 0 or 5. Now, $d_6d_7d_8$ must be divisible by 11. There is no two-digit multiple of 11 that doesn't have repeated digits, so $d_6$ cannot be 0, and must be 5.

There are eight multiples of 11 between 500 and 599, without repeated digits: 506, 517, 528, 539, 561, 572, 583 and 594.

But $d_7d_8d_9$ must be divisible by 13. This eliminates 506 from the above list, because that would require $d_9$ to also be 5. 517 is also eliminated because 17x is not divisible by 13. And 561 and 594 are eliminated because they would require $d_9$ to be 1 and 9, respectively.

This leaves the following possibilities for $d_6d_7d_8d_9$: 5286, 5390, 5728 and 5832.

Next, we know what $d_8d_9d_{10}$ must be divisible by 17. This eliminates 5832 from the above list, because that would require $d_{10}$ to be 3. So we are left with the following three possibilities for the last 5 digits: 52867, 53901 and 57289

Now consider $d_5$. $d_5d_6d_7$ must be divisible by 7. The only three-digit multiples of 7 with no repeated digits, 5 as the middle digit and 2, 3 or 7 as the last digit are 357 and 952. So we can narrow down to only two possibilities for the last 6 digits: 357289 or 952867.

Further, $d_3d_4d_5$ must be divisible by 3. Since $d_5$ is either 3 or 9, it follows that $d_3 + d_4$ must be divisible by 3. Also, $d_4$ must be even because $d_2d_3d_4$ must be divisible by 2.

In case of numbers ending in 357289, this means $d_3d_4$ must be 06 or 60. In case of numbers ending in 952867, $d_3d_4$ can only be 30. In all cases, $d_1$ and $d_2$ are 1 and 4, in any order.

So finally, we end up with the following numbers: 1406357289, 1460357289, 4106357289, 4160357289, 1430952867 and 4130952867.

Add them up to get the answer!
