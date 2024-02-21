# Path Sum: Two Ways
This problem can be solved using [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), but since we can only move right or down, there is no way to visit an already visited node. Also, the number of nodes isn't that large, so we can use a simpler, brute force approach.

Starting at top left and moving right and down, calculate the shortest path to each node from any of its neighbours. There are only two ways to reach a node, from node above it and from the node to its left. So find the neighbour with the shortest distance and add the number of the current node, this is the shortest distance to the current node. Continue like this until you reach the bottom right.

In other words, let $M$ be the original matrix. Create a new matrix $D$, such that:

$$
D[i][j] = M[i][j] + min(D[i - 1][j], D[i][j - 1])
$$
