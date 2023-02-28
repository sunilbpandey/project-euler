# Largest product in a grid
This problem is straightforward to solve. One tiny optimization is that instead of checking all eight directions, we need to check only four.

If you check the numbers to the right,

$$
55 > 58 > 88 > 24
$$

there is no need to check the numbers to the left,

$$
55 < 58 < 88 < 24
$$

since they will return the same product.
