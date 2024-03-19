# Square Digit Chains

Although this problem can be solved using brute force, it will be slow. Let's look at some optimizations.

First, note that the largest number is 9,999,999, and the sum of square of its digits is $9^2 * 7 = 567$. So if we build the chain for every number from 1 to 567, we can easily calculate the end number for all remaining numbers.

Now, the order of digits does not matter. The sum of square of digits of 1723 is the same as that of 3127, and also the same as that of 301270. So, if we find one such set of digits whose chain ends in 89, we know that all permutations of those digits will also give us the same answer.

Given a set of $N$ items, such that there are $n_1$ duplicate items of one type, $n_2$ duplicate items of second type, ..., $n_k$ duplicate items of $k^{th}$ type, the total number of permutations is given by:

$$
\frac{N!}{n_1! n_2! \dots n_k!}
$$

So, we just need to construct all numbers, $d_1d_2d_3d_4d_5d_6d_7$, where $0 \le d_1 \le d_2 \le d_3 \le d_4 \le d_5 \le d_6 \le d_7 \lt 10$, check if the chain ends in 89, and if so, increment the count appropriately.

