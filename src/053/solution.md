# Combinatoric selections
If the programming language supports very large numbers, this problem can be easily solved with a brute force approach of simply computing ${n \choose r}$ for all values of $n$ and $r$.

But with some analysis, we can avoid most of the computations.

Consider $r = 0$,

$$
{n \choose 0} = \frac{n!}{0!n!} = 1
$$

That is, there is exactly 1 way to choose 0 items out of n.

Now consider $1 \le r \le 3$,

$$
{n \choose 1} = \frac{n!}{1!(n - 1)!} = n
$$

$$
{n \choose 2} = \frac{n!}{2!(n - 2)!} = \frac{n(n - 1)}{2}
$$

$$
{n \choose 3} = \frac{n!}{3!(n - 3)!} = \frac{n(n - 1)(n - 2)}{6}
$$

It's easy to see that for $n \le 100$, none of these will be greater than 1000000.

Also, note that,

$$
{n \choose n-r} = \frac{n!}{(n - r)!(n - (n - r))!} = \frac{n!}{(n - r)!r!} = {n \choose r}
$$

This means for any $n$, we are looking for $4 \le r \le n - 4$.

Next, consider ${n \choose r + 1}$,

$$
{n \choose r + 1} = \frac{n!}{(r + 1)!(n - r - 1)!} = {n \choose r} \times \frac{n - r}{r + 1}
$$


So, ${n \choose r + 1} \ge {n \choose r}$ if,

$$
(n - r) \ge (r + 1)
$$

or,

$$
r \le \frac{n - 1}{2}
$$

Combining all that, if ${n \choose r}$ is greater than 1000000 for some $r = m$, it will be greater than 1000000 for all values of $r$ from $m$ to $n - m$. For this $n$, there will be $n - 2m + 1$ such values of $r$.

So, for each $n$, we just need to find the first value of $r$ such that ${n \choose r} > 1000000$.
