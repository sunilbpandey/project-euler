# Odd period square roots
Let, $r = \sqrt{N}$.

We can write each term in the sequence as,

$$
a_k = m_k + \frac{r + p_k}{q_k}
$$

Starting with,

$$
a_0 = \lfloor r \rfloor + r - \lfloor r \rfloor
$$

To find the next term in the sequence,

$$
a_{k + 1} = \frac{q_k}{r + p_k}
$$

Multiply both numerator and denominator with $r - p_k$,

$$
a_{k + 1} = \frac{q_k(r - p_k)}{N - p_k^2} = \frac{r - p_k}{\frac{N - p_k^2}{q_k}} = \frac{r - p_k}{q_{k + 1}}
$$

Let,

$$
q_{k + 1} = \frac{N - p_k^2}{q_k}
$$

$$
m_{k + 1} = \lfloor\frac{r - p_k}{q_{k + 1}}\rfloor
$$

and,

$$
p_{k + 1} = -p_k - m_{k + 1}q_{k + 1}
$$

Then we can write,

$$
a_{k + 1}  = m_{k + 1} + \frac{r + p_{k + 1}}{q_{k + 1}}
$$

## Eliminating some cases
### $N = m^2$
Any number that is a perfect square, i.e. $N = m^2$, will have a period of 0, so we don't need to test such numbers.

### $N = m^2 + 1$
Let, $N = m^2 + 1$, where $m$ is an integer.

So, the first term is,

$$
a_0 = m + (r - m)
$$

and the next term is,

$$
a_1 = \frac{1}{r - m} = \frac{r + m}{N - m^2} = 2m + (r - m)
$$

So we can see that any number of the form $m^2 + 1$ will result in the continued fraction $[m; (2m)]$, with a period of 1.

### $N = m^2 - 1$
Now, let $N = m^2 - 1$, for m > 1.

Or,

$N = (m - 1)^2 + 2m - 2$.

This gives us,
$$
a_0 = (m - 1) + r - (m - 1)
$$

and,

$$
a_1 = \frac{1}{r - m + 1} = \frac{r + m - 1}{N - (m - 1)^2} = 1 + \frac{r - m + 1}{2m - 2}
$$

and,

$$
a_2 = \frac{2m - 2}{r - m + 1} = \frac{(2m - 2)(r + m - 1)}{N - (m - 1)^2} = r + m - 1 = 2(m - 1) + r - (m - 1)
$$

As we can see, this will produce the continued fraction $[(m - 1); (1, 2m - 2)]$, with a period of 2.

### $N = m^2 + 2$
Now, let $N = m^2 + 2$

So,

$$
a_0 = m + (r - m)
$$

and,

$$
a_1 = \frac{1}{r - m} = \frac{r + m}{N - m^2} = \frac{r + m}{2} = m + \frac{r - m}{2}
$$

and,

$$
a_1 = \frac{2}{r - m} = \frac{2(r + m)}{N - m^2} = r + m = 2m + (r - m)
$$

As we can see in this case, we will get a continued fraction $[m; (m, 2m)]$, with a period of 2.

### $N = m^2 - 2$
Now, let $N = m^2 - 2$, for m > 2.

Or,

$N = (m - 1)^2 + 2m - 3$

So,

$$
a_0 = (m - 1) + (r - m + 1)
$$

and,

$$
a_1 = \frac{1}{r - m + 1} = \frac{r + m - 1}{N - (m - 1)^2} = \frac{r + m - 1}{2m - 3} = 1 + \frac{r - m + 2}{2m - 3}
$$

and,

$$
a_2 = \frac{2m - 3}{r - m + 2} = \frac{(2m - 3)(r + m - 2)}{N - (m - 2)^2} = \frac{(2m - 3)(r + m - 2)}{4m - 6} = \frac{r + m - 2}{2} = m - 2 + \frac{r - m + 2}{2}
$$

and,

$$
a_3 = \frac{2}{r - m + 2} = \frac{2(r + m - 2)}{N - (m - 2)^2} = \frac{2(r + m - 2)}{4m - 6} = \frac{r + m - 2}{2m - 3} = 1 + \frac{r - m + 1}{2m - 3}
$$

and,

$$
a_4 = \frac{2m - 3}{r - m + 1} = \frac{(2m - 3)(r + m - 1)}{N - (m - 1)^2} = r + m - 1 = (2m - 2) + r - m + 1
$$

So, in this case we will get a continued fraction $[(m - 1); (1, m - 2, 1, 2m - 2)]$, with a period of 4.
