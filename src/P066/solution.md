# Diophantine equation
Any Diophantine equation of the form $x^2 - ny^2 = 1$ is also known as [Pell's equation](https://en.wikipedia.org/wiki/Pell%27s_equation).

The minimal solution in x can be found using the [convergents](https://en.wikipedia.org/wiki/Convergent_(continued_fraction)) for $\sqrt{n}$.

If $\frac{h_i}{k_i}$ denotes the sequence of convergents for $\sqrt{n}$, then the minimal solution in x equals $h_i$ for some $i$. It can be found by generating convergents until we find a pair (h, k) such that $h^2 - nk^2 = 1$.

To generate the convergents, we can use the same method as we used in [problem 65](/src/065).
