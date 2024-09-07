# Pandigital products
We are looking for an identity of the form,

$$
m * n = p
$$

Since the order doesn't matter in multiplication, let's say $m \le n$.

If $m \ge 100$, that means $n \ge 100$, therefore $p \ge 10000$. But this means the entire identity will have 11 or more digits. Since our identity should have exactly 9 digits, $m < 100$.

If $p < 1000$, that must mean $n < 1000$. But since $m < 100$, that means the identity will have at most 8 digits. Therefore, $p \ge 1000$.

Now, if $p \ge 10000$, that must mean $n \ge 100$ if $10 \le m \lt 100$, and $n \ge 1000$ if $m < 10$. But in both cases, the identity will have at least 10 digits. Therefore, $p < 10000$.

Now we can go through all possible values of $m$ and $n$, until we find the identity.
