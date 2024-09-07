# pylint: disable=invalid-name
# pylint: disable=too-many-branches
# pylint: disable=too-many-nested-blocks
import math


def sum_of_squares(digits: list[int]) -> int:
    return sum(d**2 for d in digits)


def sum_of_square_of_digits(n: int) -> int:
    return sum_of_squares([int(d) for d in str(n)])


def solve() -> int:
    chain_end = [-1] * 568
    chain_end[1] = 1
    chain_end[89] = 89

    for n in range(2, 568):
        digit_sum = sum_of_square_of_digits(n)
        while chain_end[digit_sum] == -1:
            digit_sum = sum_of_square_of_digits(digit_sum)
        chain_end[n] = chain_end[digit_sum]

    count = 0
    for d1 in range(10):
        for d2 in range(d1, 10):
            for d3 in range(d2, 10):
                for d4 in range(d3, 10):
                    for d5 in range(d4, 10):
                        for d6 in range(d5, 10):
                            for d7 in range(d6, 10):
                                digit_sum = sum_of_squares([d1, d2, d3, d4, d5, d6, d7])
                                if chain_end[digit_sum] == 89:
                                    digits = [0] * 10
                                    for d in (d1, d2, d3, d4, d5, d6, d7):
                                        digits[d] += 1
                                    denominator = 1
                                    for d in digits:
                                        if d > 0:
                                            denominator *= math.factorial(d)
                                    count += math.factorial(7) // denominator
    return count
