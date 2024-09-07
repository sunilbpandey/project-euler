from src.utils.py.math import proper_divisors


def is_amicable(num: int) -> bool:
    divisor_sum = sum(proper_divisors(num))
    return divisor_sum != num and sum(proper_divisors(divisor_sum)) == num


def solve() -> int:
    return sum(num for num in range(2, 10001) if is_amicable(num))
