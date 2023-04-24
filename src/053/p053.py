import math


def solve1() -> int:
    total = 0
    # pylint: disable=invalid-name
    for n in range(23, 101):
        for r in range(n):
            if math.comb(n, r) > 1000000:
                total += 1
    # pylint: enable=invalid-name
    return total


def solve() -> int:
    total = 0
    # pylint: disable=invalid-name
    for n in range(23, 101):
        r = next(r for r in range(4, n - 3) if math.comb(n, r) > 1000000)
        total += n - 2 * r + 1
    # pylint: enable=invalid-name
    return total
