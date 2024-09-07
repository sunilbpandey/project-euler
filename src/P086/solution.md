# Cuboid Route
Consider a cuboid of dimensions a x b x c. Since the route must be along the surfaces of the cuboid, flatten the sides, creating a rectangle with the spider and the fly on the opposite ends of the diagonal. By choosing which side to flatten, we can make one of three rectangles:

    a + b x c
    a + c x b
    b + c x a

The distance to travel is the length of the diagonal of this rectangle. So we need to find the rectangle out of these three which has the shortest diagonal.

Assume, $0 \lt a \le b \le c$.

The length of the diagonal of a rectangle measuring a x b is $\sqrt{a^2 + b^2}$.

So comparing the square of the length of the diagonal of the three rectangles above, we get:

$$
(a + b)^2 + c^2 = a^2 + b^2 + c^2 + 2ab\\
(a + c)^2 + b^2 = a^2 + b^2 + c^2 + 2ac\\
(b + c)^2 + a^2 = a^2 + b^2 + c^2 + 2bc
$$

Since $a \le b \le c$, we can see that the shortest path must be in the a + b x c rectangle, and its length will be $\sqrt{(a + b)^2 + c^2}$.

At this point, we can iterate over all values of a, b and c where $\sqrt{(a + b)^2 + c^2}$ is an integer.

But we don't need to check every value of a and b, since we are only interested in their sum. Once we find a value of $a + b$ which works, we can find all values of $a$ and $b$, which will produce the same sum.

To make sure that we check each sum exactly once, we can iterate in the following manner:

- Start with $a = 1$, $b = 2$ and $c = 2$. It's easy to see that no solution is possible if $a == 1$ and $b == 1$.
- Check if $\sqrt{(a + b)^2 + c^2}$ is an integer
    - If it is, increment the count of solutions by $\frac{b - a}{2} + 1$. This is explained below.
- If $a == b == c$, has the count of solutions reached one million?
    - If yes, then the answer is $c$
    - Otherwise, increment $c$ and reset $a$ and $b$ back to 1 and 2, respectively.
- Otherwise, if $b \lt c$, increment $b$.
- Otherwise, increment $a$.

Iterating in this manner ensures that, for every value of $c$, $a + b$ is steadily incremented by 1 on every iteration, starting at $a + b = 3$.

Once we find a suitable value of $a + b$, because of the way we are incrementing, we know that this must be the smallest value of $a$. Any smaller values of $a$ will make $b > c$.

So, given the sum $a + b$, there are $\frac{a + b}{2}$ possible values of $a$, out of which $a - 1$ values must be discarded. This gives us the count $\frac{b - a}{2} + 1$.

## Alternative approach
Observe that (a + b), c and the diagonal form a Pythagorean triple. So this can also be solved by using [Euclid's formula](https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple) to generate Pythagorean triples.
