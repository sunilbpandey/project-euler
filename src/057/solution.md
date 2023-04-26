# Square root convergents
Observe the first seven expansions: $\frac{3}{2}$, $\frac{7}{5}$, $\frac{17}{12}$, $\frac{41}{29}$, $\frac{99}{70}$, $\frac{239}{169}$, $\frac{577}{408}$.

It's easy to see the recurrence between the numerators and denominators.

Let, $n_k$ be the $k^{th}$ numerator and $d_k$ be the $k_{th}$ denominator.

Let, $n_0 = 1$ and $d_0 = 1$.

Then we have,

$d_1 = n_0 + d_0$

and,

$n_1 = d_0 + d_1$

We can use these two equations to easily calculate terms up to $n_{1000}$ and $d_{1000}$.

But we can take this one step further.

Observe,

$d_{k + 1} = n_k + d_k$

and,

$n_{k + 1} = d_k + d_{k + 1}$

Combining, we get,

$d_{k + 1} = 2d_k + d_{k - 1}$

and,

$n_{k + 1} = 2d_k + n_k$

Expanding $d_k$, we get,

$n_{k + 1} = 2n_{k - 1} + 2d_{k - 1} + n_k = n_{k - 1} + (n_{k - 1} + 2d_{k - 1}) + n_k$

Or,

$n_{k + 1} = 2n_k + n_{k - 1}$

So we have the two recurrence relations,

$n_{k + 2} = 2n_{k + 1} + n_k$

$d_{k + 2} = 2d_{k + 1} + d_k$

Say, the solution is of the form $r^k$ for some $r > 0$.

Plugging into our recurrence equation,

$r^k - 2r^{k - 1} - r^{k - 2} = 0$

Or,

$r^{k - 2}(r^2 - 2r - 1) = 0$

Since $r > 0$, this means,

$r^2 - 2r - 1 = 0$

the roots of which are given by the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula),

$r = 1 \pm \sqrt{2}$

Given the two roots, the solution to the recurrence relation is given by,

$a_k = Ar_1^k + Br_2^k$

where $A$ and $B$ are constants determined by the initial conditions.

In our case, let $r_1 = 1 + \sqrt{2}$ and $r_2 = 1 - \sqrt{2}$.

For simplicity, let the initial conditions be, $n_0 = 1, n_1 = 1$ and $d_0 = 0, d_1 = 1$.

Plugging these initial conditions into the equation for numerator, we get $A + B = 1$ and $A - B = 0$, which gives us $A = \frac{1}{2}$ and $B = \frac{1}{2}$.

Solving for denominator, we get $A + B = 0$ and $A - B = \frac{1}{\sqrt{2}}$, which gives us $A = \frac{1}{2\sqrt{2}}$ and $B = -\frac{1}{2\sqrt{2}}$.

So, we finally have the two equations,

$n_k = \frac{r_1^k + r_2^k}{2}$

and,

$d_k = \frac{r_1^k - r_2^k}{2\sqrt{2}}$

where $r_1 = 1 + \sqrt{2}$ and $r_2 = 1 - \sqrt{2}$.

Now, the number of digits in a number $m$ is $\lfloor{\log_{10}m\rfloor} + 1$, where $\lfloor\rfloor$ denote the [floor function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions).

So,

$\text{CountOfDigits}(n_k) = 1 + \lfloor k\log_{10}r_1 + \log_{10}(1 + (\frac{r_2}{r_1})^k) - \log_{10}2\rfloor$

and,

$\text{CountOfDigits}(d_k) = 1 + \lfloor k\log_{10}r_1 + \log_{10}(1 - (\frac{r_2}{r_1})^k) - \frac{3}{2}\log_{10}2\rfloor$

Finally,

$\frac{r_2}{r_1} = \frac{1 - \sqrt{2}}{1 + \sqrt{2}}$

multiplying both numerator and denominator by $r_2$, we get,

$\frac{r_2}{r_1} = 2\sqrt{2} - 3$

Now we are ready to compute the terms and count their digits. Note that because of how we set the initial conditions, the first term in the problem is given by $k = 2$, so we need to compute the terms until $k = 1001$.
