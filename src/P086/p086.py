# pylint: disable=invalid-name
import math


def is_perfect_square(num: int) -> bool:
    return int(math.sqrt(num)) ** 2 == num


def solve() -> int:
    count = 0
    # pylint: disable=invalid-name
    a, b, c = 1, 2, 2
    while True:
        d = (a + b) ** 2 + c**2
        if is_perfect_square(d):
            count += ((b - a) // 2) + 1
        if a == b and b == c:
            if count > 1000000:
                return c
            a, b, c = 1, 2, c + 1
        elif b < c:
            b += 1
        else:
            a += 1
