import math


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
