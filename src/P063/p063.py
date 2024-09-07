import itertools
import math


def solve1() -> int:
    count = 0
    # pylint: disable=invalid-name
    for m in range(1, 10):
        for n in itertools.count(1):
            digit_count = len(str(m**n))
            if digit_count == n:
                count += 1
            elif digit_count < n:
                break
    # pylint: enable=invalid-name
    return count


def solve() -> int:
    return sum(math.floor(1 / (1 - math.log10(m))) for m in range(1, 10))
