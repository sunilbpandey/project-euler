# Spiral primes
Reusing the analysis from problem [28](/src/028), the spiral is formed by concentric layers:

```
1
2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
```

Let the innermost layer correspond to $n = 0$. We can see that the side length of $n^{th}$ layer is $2n + 1$.

By construction, the last number of a layer is at the bottom right corner, and it equals $(2n + 1)^2$. Clearly, this number can never be prime.

To calculate the numbers at the four corners in the $n^{th}$ layer, take the last number of the previous layer and add $2n$, $4n$, $6n$ and $8n$ to it. Again, the last number of this layer will not be prime, so we only need to test the other three.
