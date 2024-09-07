# Number spiral diagonals
The spiral is formed by layers of concentric squares:

    1
    2 3 4 5 6 7 8 9
    10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

Starting with $n = 0$, $n^{th}$ layer has $2n + 1$ numbers on each side. At the end of this layer, there are a total of $2n + 1$ rows and $2n + 1$ columns, so altogether $(2n + 1)^2$ numbers.

By construction, the last number of a layer is on the top right corner, so the top right corner of $n^{th}$ layer must be $(2n + 1)^2$. From this we can calculate other corners.

Top right = $(2n + 1)^2$ = $4n^2 + 4n + 1$

Top left = $(2n + 1)^2 - 2n$ = $4n^2 + 2n + 1$

Bottom left = $(2n + 1)^2 - 4n$ = $4n^2 + 1$

Bottom right = $(2n + 1)^2 - 6n$ = $4n^2 - 2n + 1$

Diagonal sum for each layer = $16n^2 + 4n + 4$

Since we are looking for spiral with 1001 numbers on each side, the final layer corresponds to $n = 500$.
