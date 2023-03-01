# Longest Collatz sequence
The key insights here is that we don't need to recalculate the chain lengths for every number; caching chain lengths for smaller values will greatly speed up the calculation for larger numbers.

Also, the sequence starting at $2n$ will, by definition, be one longer than the sequence starting at $n$. So, we can start the search at 500,000. This doesn't give us any significant benefit in practice, however, because we will end up calculating the chain lengths for most of the smaller numbers anyway.
