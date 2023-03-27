def find_cycle_length(denominator: int) -> int:
    numerator = 1
    seen: dict[int, int] = {}
    while numerator > 0:
        numerator = (numerator * 10) % denominator
        if numerator in seen:
            return len(seen) - seen[numerator]
        seen[numerator] = len(seen)
    return 0


def solve1() -> int:
    max_cycle = 0
    max_cycle_denominator = 0
    for denominator in range(2, 1000):
        cycle_length = find_cycle_length(denominator)
        if cycle_length > max_cycle:
            max_cycle = cycle_length
            max_cycle_denominator = denominator
    return max_cycle_denominator


def solve() -> int:
    max_cycle = 0
    max_cycle_denominator = 0
    for denominator in range(2, 1000):
        if denominator % 2 == 0 or denominator % 5 == 0:
            continue
        cycle_length = 1
        power = 10
        while (power - 1) % denominator != 0:
            power *= 10
            cycle_length += 1
        if cycle_length > max_cycle:
            max_cycle = cycle_length
            max_cycle_denominator = denominator
    return max_cycle_denominator
