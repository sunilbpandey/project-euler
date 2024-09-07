import itertools
import math
from src.utils.py.series import convergents, e_continued_fraction


def solve1() -> int:
    term = 100
    num = 3 if term % 3 == 0 else 1
    den = 2 * term if term % 3 == 0 else 1

    for i in range(term - 1, 1, -1):
        if i % 3 == 0:
            # add 2*i/3 to the fraction
            num += 2 * (i // 3) * den
        else:
            # add 1 to the fraction
            num += den
        num, den = den, num
    num += 2 * den

    # simplify the fraction
    gcd = math.gcd(num, den)
    num, den = num // gcd, den // gcd
    return sum(int(digit) for digit in str(num))


def solve() -> int:
    numerator, _ = next(itertools.islice(convergents(e_continued_fraction()), 99, None))
    return sum(int(digit) for digit in str(numerator))
