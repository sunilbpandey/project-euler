import itertools
from src.utils.py.series import fibonacci


def solve() -> int:
    return sum(
        n for n in itertools.takewhile(lambda n: n < 4000000, fibonacci()) if n % 2 == 0
    )
