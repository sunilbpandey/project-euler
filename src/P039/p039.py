import math


def solve1() -> int:
    solutions = [0] * 1001
    # pylint: disable=invalid-name
    for p in range(2, 1001, 2):
        for a in range(1, p // 2):
            n = p**2
            d = 2 * (p - a)
            if n % d != 0:
                continue
            b = p + n // d
            if b > a:
                solutions[p] += 1
    # pylint: enable=invalid-name
    return solutions.index(max(solutions))


def solve() -> int:
    solutions = [0] * 1001
    # pylint: disable=invalid-name
    for m in range(2, 22):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            p = 2 * m * (m + n)
            for k in range(1, 1000 // p + 1):
                solutions[k * p] += 1
    # pylint: enable=invalid-name
    return solutions.index(max(solutions))
