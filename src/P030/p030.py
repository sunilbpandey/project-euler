from itertools import combinations_with_replacement, product


FIFTH_POWERS = [d**5 for d in range(10)]


def solve1() -> int:
    total = 0
    # pylint: disable=invalid-name
    for a, b, c, d, e, f in product(range(10), repeat=6):
        num = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
        if a**5 + b**5 + c**5 + d**5 + e**5 + f**5 == num:
            if num > 1:
                total += num
    # pylint: enable=invalid-name
    return total


def solve() -> int:
    total = 0
    for length in range(2, 7):
        for combo in combinations_with_replacement(range(10), length):
            powersum = sum(FIFTH_POWERS[d] for d in combo)
            powersum_digits = sorted([int(d) for d in str(powersum)])
            combo_digits = sorted(combo)
            if powersum_digits == combo_digits:
                total += powersum
    return total
