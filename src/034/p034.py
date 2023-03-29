from itertools import combinations_with_replacement
import math


DIGIT_FACTORIALS = [math.factorial(d) for d in range(10)]


def solve() -> int:
    total = 0
    for length in range(2, 8):
        for combo in combinations_with_replacement(range(10), length):
            factorial_sum = sum(DIGIT_FACTORIALS[d] for d in combo)
            factorial_sum_digits = sorted([int(d) for d in str(factorial_sum)])
            combo_digits = sorted(combo)
            if factorial_sum_digits == combo_digits:
                total += factorial_sum
    return total
