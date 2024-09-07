# Smallest multiple

We need to find [LCM](https://en.wikipedia.org/wiki/Least_common_multiple) of set of numbers. There are a few different ways to solve this.

## Prime factorization

Express each number in terms of its prime factors:

```
4 = 2^2
15 = 3^1 * 5^1
18 = 2^1 * 3^2
etc.
```

The LCM will the product of the highest power of each prime number.

## Using greatest common divisor

LCM can be calculated from the [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) using this formula:

```
lcm(a, b) = a * b / gcd(a, b)
```

The GCD can be computed using [Euclid's algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm).

Also, for non-zero numbers a1, a2, ..., ak:

```
lcm(a1, a2, ..., ak) = lcm(lcm(a1, a2, ..., ak-1), ak)
```

So we can compute LCM of the first two numbers, then LCM of that with the third number and so on.
