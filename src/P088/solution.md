# Product-sum Numbers

Let's start by trying to find some bounds for $N$ for a given $k$.

Given,

$$
N = a_1 + a_2 + \dots + a_k
$$

Since each $a_i > 0$, it is clear that $N > k$.

Now consider, $N = 2 * k$

Let's say $a_1 = 2$ and $a_2 = k$. If we set the remaining $a_3 \dots a_k$ to 1, we can see that the total sum will become $2 + k + (k - 2) = 2k$. And of course, the product is also $2k$.

Therefore, $N = 2k$ is a guaranteed solution.

So, for a given $k$,

$$
k \lt N \le 2k
$$

For this problem, since $2 \le k \le 12000$, we know that $N \le 24000$.

Now, since $k \ge 2$, every $a_i < N$, otherwise the sum will exceed $N$. If $N$ is prime, this means the product will always be 1. Therefore, $N$ must be composite.

So we have the range for this problem, $4 \le N \le 24000$.

At this point, we can go through every number in that range, find its divisors and calculate their product and sum, but there is another approach.

Say, we calculate the product $2 * 4 = 8$, and their sum $2 + 4 = 6$. Their difference is $8 - 6 = 2$. If we fill this with two 1s, that means $8$ is a solution for $k = 4$.

So we can calculate all the products, $2 * 2, 2 * 3, 2 * 4, \dots$ until they exceed $24000$. Then calculate $3 * 3, 3 * 4, \dots$ and so on. Then calculate $2 * 2 * 2, 2 * 2 * 3, \dots$ and so on.

Since $2^{15} = 32768$, we will only need to multiply up to 14 terms.

For each product, compute the sum of the factors and the $k$ value. Then see if this product is the minimal product for that $k$.
