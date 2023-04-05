# Self powers
If the programming language supports arbitrarily large numbers, then this can be solved using the simple brute force approach of actually computing the entire sum and then taking the last 10 digits.

However, we don't need large numbers because we only need to keep track of the 10 least significant digits. So we can implement our own "power" function, which repeatedly multiplies the number and tracks only the last 10 digits.
