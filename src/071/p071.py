import math


def solve() -> int:
    fractions = (((d * 3 - 1) // 7, d) for d in range(2, 1000001))
    largest_fraction = max(fractions, key=lambda f: f[0] / f[1])
    return largest_fraction[0] // math.gcd(*largest_fraction)
