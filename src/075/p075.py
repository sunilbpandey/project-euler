import math


def solve() -> int:
    solutions = [0] * 1500001
    # pylint: disable=invalid-name
    for m in range(2, 867):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            L = 2 * m * (m + n)
            for k in range(1, 1500000 // L + 1):
                solutions[k * L] += 1
    # pylint: enable=invalid-name
    return solutions.count(1)
