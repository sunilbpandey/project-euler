from src.utils.py.math import is_palindrome


def is_lychrel_number(num: int) -> bool:
    for _ in range(50):
        num += int(str(num)[::-1])
        if is_palindrome(num):
            return False
    return True


def solve() -> int:
    count = 0
    for num in range(1, 10000):
        if is_lychrel_number(num):
            count += 1
    return count
