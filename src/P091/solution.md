# Right Triangles with Integer Coordinates

This problem can be solved using brute force. There are 51 possibilities each for x1 and y1, but since P cannot be a (0, 0), there are 51 x 51 - 1 = 2600 possible points for P. Similarly, there are 2600 possibilities for Q. Multiplying the two numbers, we get 6,760,000 possible triangles that we must examine.

To check whether a triangle is right triangle, calculate the square of the length of each side and check if any two of the sides add up to the third one.

If P is at $(x_1, y_1)$ and Q is at $(x_2, y_2)$, the length of the side PQ is given by:

$$
\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

And the lengths of the sides OP and OQ are $\sqrt{x_1^2 + y_1^2}$ and $\sqrt{x_2^2 + y_2^2}$ respectively.

Since P and Q can be swapped, this list will contain duplicates, and so the count will be twice the actual number. We can avoid these duplicates by keeping $y_2 \le y_1$ and $x_2 \ge x_1$.

## Alternative approach

There is a more efficient approach. 

First, consider all the rectangles formed by $(0, 0)$, $(0, y_1)$, $(x_2, y_1)$, and $(x_2, 0)$. There are 50 possible values for $x_2$ and 50 possible values for $y_1$, so there are 50 x 50 = 2500 such rectangles:

    A . B
    .   .
    .   .
    O . C

This rectangle contains three right triangles which include the point O: OAC, OAB and OBC. Therefore, there are 3 x 2500 = 7500 right triangles formed this way.

Now consider all triangles where the right angle is at P, and P is not on either of the axes. Let's say P is at the point $(x, y)$. So the slope of the line OP is $\frac{y}{x}$. For PQ to be perpendicular to OP, the slope of the line PQ must be $-\frac{x}{y}$. Note that $-\frac{x}{y}$ may need to be simplified.

So, given a point P, we need to enumerate all values of Q. To do this, starting at P, we need to go down by $x$ and to the right by $y$, and keep doing this until the resulting coodinates are outside the range $0 \le x, y \le 50$.

Since we are starting at $(x, y)$ and going down by $x$ at every step, we can only go down $x$ steps. And since we are going right by $y$ at every step, we can only go $\lfloor{\frac{50 - x}{y}}\rfloor$ steps to the right. The minimum of these two numbers gives us the number of possible values of Q.

Finally, consider all triangles where the right angle is at Q, and Q is not on either of the axes. We can see that all these triangles are just mirror images of the triangles constructed above, so we can just double the number of triangles we found above.
