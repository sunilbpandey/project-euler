# Maximum path sum I
As the problem mentions, this can be solved using brute force, but there is a clever method for solving it.

Consider a number on the second last row. This number has two descendants. The maximum total of any path containing this number is the sum of the maximum total of the path up to this number and the maximum total starting at this number. The maximum total starting at this number is simply the sum of this number and the greater of its two descendants.

So take each number on the second last row, and add to it the greater of its two descendants. This way, we collapse the last row of the triangle into the second last row. Continue upwards in this manner until we reach the top row.
