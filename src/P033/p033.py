import math


def solve() -> int:
    numerator = 1
    denominator = 1
    # pylint: disable=invalid-name
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(b + 1, 10):
                if 10 * a * c == 9 * c * b + a * b:
                    numerator *= 10 * a + b
                    denominator *= 10 * c + a

                if 10 * a * b == 9 * b * c + a * c:
                    numerator *= 10 * b + a
                    denominator *= 10 * a + c
    # pylint: enable=invalid-name
    return denominator // math.gcd(numerator, denominator)
