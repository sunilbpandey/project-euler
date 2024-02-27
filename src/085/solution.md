# Counting Rectangles
There are at least a couple of ways to solve this.

## Counting rectangles
A 3x2 grid has 12 vertices

    *    *    *    *
    *    *    *    *
    *    *    *    *

In general, an m x n grid has m + 1 vertices in each row and n + 1 vertices in each column. The smallest rectangle has width and height of 1. The largest rectangle has width m and height n.

To form a rectangle of width w and height h, we just need to decide where the top-left corner should be. Since the width is w, the top-left corner can only be in one of the left-most m + 1 - w columns. Similarly, it can only be in one of the top n + 1 - h rows. Altogether, we can form (m + 1 - w) * (n + 1 - h) rectangles of width w and height h.

Go through all values of w and h, and count the number of rectangles that can be formed.

## Direct calculation
We can also calculate the number more directly. A 3x2 grid is formed by drawing 3 horizontal lines and 4 vertical lines

    ----------------
    |    |    |    |
    ----------------
    |    |    |    |
    ----------------
    |    |    |    |
    ----------------

To form a rectangle, we need to pick two of the horizontal lines, and two of the vertical lines (and ignore the parts of the lines that extend beyond the intersecting areas). The two horizontal lines can be selected in C(4, 2) ways, or 6 ways. The two vertical lines can be selected in C(3, 2) ways, or 3 ways. Multiplying gives us the answer: 18.

In general, the number of rectangles contained in an m x n grid is C(m + 1, 2) * C(n + 1, 2). And since C(n, 2) = n * (n - 1) / 2, the number of rectangles is: m(m + 1)n(n + 1) / 4.

### Upper bounds
Since a 3x2 grid will have the same number of rectangles as a 2x3 grid, we only need to check grids where height is less than or equal to the width.

Now consider an m x 1 grid. This grid has m(m + 1)/2 rectangles. This gives us an upper bound of 2000 for the width. Any larger grid will have more than two million rectangles.
