# Digit cancelling fractions
We are looking for fractions of the form:

$$
\frac{ab}{ac}, \frac{ab}{ca}, \frac{ba}{ac}, \frac{ba}{ca}
$$

In all cases, the fraction must simplify to $\frac{b}{c}$. Since we are looking for fractions less that one in value, $b < c$.

Consider fractions of the form $\frac{ab}{ac}$. If,

$$
\frac{10a + b}{10a + c} = \frac{b}{c}
$$

that means,

$$
10ac + bc = 10ab + bc
$$

or,

$$
b = c
$$

which contradicts $b < c$, so we can eliminate this case.

Now consider $\frac{ba}{ca}$. If,

$$
\frac{10b + a}{10c + a} = \frac{b}{c}
$$

that means,

$$
10bc + ac = 10bc + ab
$$

or,

$$
c = b
$$

Again, we can eliminate this case too.

This leaves two cases,

$$
\frac{ab}{ca}, \frac{ba}{ac}
$$

Consider $\frac{ab}{ca}$.

$$
\frac{10a + b}{10c + a} = \frac{b}{c}
$$

gives us,

$$
10ac = 9bc + ab
$$

where $a > 0$ and $0 < b < c \le 9$.

Finally, consider $\frac{ba}{ac}$.

$$
\frac{10b + a}{10a + c} = \frac{b}{c}
$$

gives us,

$$
10ab = 9bc + ac
$$

where $a > 0$ and $0 < b < c \le 9$.
