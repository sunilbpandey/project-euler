import math
from src.utils.py.math import lcm


def solve1() -> int:
    smallest_multiple = 1
    for i in range(2, 21):
        smallest_multiple = lcm(smallest_multiple, i)
    return smallest_multiple


def solve() -> int:
    # lcm from standard library is much faster
    return math.lcm(*range(2, 21))
