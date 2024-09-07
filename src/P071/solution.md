# Ordered fractions
Consider the fraction $\frac{a}{b}$. We want to find the largest fraction $\frac{c}{d}$ such that $\frac{c}{d} < \frac{a}{b}$ and $d \le N$, for some $N$.

For a given $d$, we can solve for $c$,

$$
bc < ad
$$

Or,

$$
bc \le ad - 1
$$

which gives us,

$$
c \le \lfloor \frac{ad - 1}{b} \rfloor
$$

For this problem, $a = 3$, $b = 7$ and $d \le 1000000$.

So for all values of $7 \lt d \le 1000000$, calculate $c$ and find the value of $c$ corresponding to the largest fraction. Note that $\frac{c}{d}$ may need to be reduced.
