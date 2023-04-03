import math
from src.utils.py.series import pentagonal_numbers, triangle_numbers


def is_pentagonal_number(number: int) -> bool:
    root = math.sqrt(24 * number + 1)
    return root % 1 == 0 and (int(root) + 1) % 6 == 0


def is_hexagonal_number(number: int) -> bool:
    root = math.sqrt(8 * number + 1)
    return root % 1 == 0 and (int(root) + 1) % 4 == 0


def solve1() -> int:
    for num in triangle_numbers():
        if num > 40755 and is_pentagonal_number(num) and is_hexagonal_number(num):
            return num
    raise RuntimeError("No solution found")


def solve() -> int:
    for num in pentagonal_numbers():
        if num > 40755 and is_hexagonal_number(num):
            return num
    raise RuntimeError("No solution found")
