import math
from src.utils.py.series import fibonacci


def solve1() -> int:
    index = 0
    for num in fibonacci():
        index += 1
        if len(str(num)) >= 1000:
            break
    return index


def solve() -> int:
    phi = (1 + math.sqrt(5)) / 2
    return round((999 * math.log(10) + math.log(5) / 2) / math.log(phi))
