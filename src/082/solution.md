# Path Sum: Three Ways
One way to solve this problem is using [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), applying it multiple times for each pair of starting and ending cells, but that turns out to be very slow.

Here's another approach, which is faster, although not the fastest way to solve this problem.

Consider two columns:

    0   5
    1   6
    2   7
    3   8
    4   9

And say we want to find out the minimal path sum ending on any cell in the second column. We can move up, down or right, but it doesn't make sense to move up or down the second column. Since we are dealing with only positive numbers, that would not give us the minimal sum.

So, in order to compute the minimal path sum ending on cell 7, we only need to consider the following paths:

    0 -> 1 -> 2 -> 7
    1 -> 2 -> 7
    2 -> 7
    3 -> 2 -> 7
    4 -> 3 -> 2 -> 7

To calculate the sum of each path, take the minimal path sum of the first node, then add the values of the remaining nodes, including the last node. I.e. sum of the first path is minimal path sum of node 0 + value of node 1 + value of node 2 + value of node 7. Calculate these for each path and find the minimum of these sums.

Let $M$ be the original matrix. We will create a matrix $C$ of the same size as $M$, so that $C[i][j]$ is the minimal path sum starting at any cell in the first column and ending at $i, j$.

In other words,

$$
C[i][j] = min (C[k][j - 1] + \sum_{p=k}^{i}M[p][j - 1] + M[i][j])
$$

for all values of $k$.
