import itertools
from src.utils.py.series import fibonacci


def solve1() -> int:
    return sum(
        n for n in itertools.takewhile(lambda n: n < 4000000, fibonacci()) if n % 2 == 0
    )


def solve() -> int:
    prev = 1
    curr = 1
    while curr < 4000000:
        prev, curr = curr, prev + curr

    if curr % 2 == 0:
        return (prev - 1) // 2
    if prev % 2 == 0:
        return (prev + curr - 1) // 2
    return (curr - 1) // 2
