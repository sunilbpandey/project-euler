import itertools
import math


def solve1() -> int:
    digits = ""
    for number in itertools.count():
        if len(digits) > 1000000:
            break
        digits += str(number)
    return math.prod(int(digits[10**i]) for i in range(7))


def solve2() -> int:
    # Source: https://projecteuler.net/thread=40#535
    length = 0
    product = 1
    next_n = 1
    for number in itertools.count(start=1):
        numstr = str(number)
        length += len(numstr)
        if length >= next_n:
            product *= int(numstr[next_n - length + len(numstr) - 1])
            next_n *= 10
            if next_n > 1000000:
                break
    return product


def get_champernowne_digit(index: int) -> int:
    i = 0
    for i in itertools.count():
        next_group = 9 * (i + 1) * 10**i
        if index < next_group:
            break
        index -= next_group
    number = 10**i + (index - 1) // (i + 1)
    digit = (index - 1) % (i + 1) + 1
    return int(str(number)[digit - 1])


def solve() -> int:
    return math.prod(get_champernowne_digit(10**i) for i in range(7))
