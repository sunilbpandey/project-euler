# Power digit sum
There is no clever optimization here, we do need to compute $2^{1000}$. If the programming language supports big integers, this is trivial to calculate. Some languages like Python and Haskell support this in the native integer type, some others like Javascript and Go have special "big integer" types.

If the programming language doesn't support big integers, they can be simulated using strings or arrays.
