from src.utils.py.math import proper_divisors


def solve() -> int:
    abundant = set()
    non_abundant_sum = 0
    for num in range(1, 28124):
        if sum(proper_divisors(num)) > num:
            abundant.add(num)

        # See if the number can be written as sum of existing abundant numbers
        if not any((num - a in abundant) for a in abundant):
            non_abundant_sum += num
    return non_abundant_sum
