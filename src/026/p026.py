from typing import List, Tuple


def find_cycle_length(denominator: int) -> int:
    numerator = 1
    seen: List[Tuple[int, int]] = []
    while numerator > 0:
        while numerator < denominator:
            numerator *= 10

        quotient, numerator = numerator // denominator, numerator % denominator
        if (quotient, numerator) in seen:
            return len(seen) - seen.index((quotient, numerator))
        seen.append((quotient, numerator))
    return 0


def solve() -> int:
    max_cycle = 0
    max_cycle_denominator = 0
    for denominator in range(2, 1000):
        cycle_length = find_cycle_length(denominator)
        if cycle_length > max_cycle:
            max_cycle = cycle_length
            max_cycle_denominator = denominator
    return max_cycle_denominator
