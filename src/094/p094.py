# pylint: disable=invalid-name
import math


def solve() -> int:
    perimeter_sum = 0
    for n in range(1, 15812):
        for diff in (1, -1):
            tsq = 3 * n**2 + diff
            t = int(math.sqrt(tsq))
            if t**2 == tsq:
                for m in (t, 2 * n + t):
                    if m < n or math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                        continue
                    r = m**2 + n**2
                    p = min(m**2 - n**2, 2 * m * n)
                    perimeter = 2 * (p + r)
                    if perimeter <= 1_000_000_000:
                        perimeter_sum += perimeter
    return perimeter_sum
