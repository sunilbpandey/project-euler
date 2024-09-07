import math


def solve() -> int:
    count = 0
    log_r1 = math.log10(1 + math.sqrt(2))
    log_2 = math.log10(2)

    for k in range(2, 1002):
        power = (2 * math.sqrt(2) - 3) ** k
        num_digits = 1 + math.floor(k * log_r1 + math.log10(1 + power) - log_2)
        denom_digits = 1 + math.floor(k * log_r1 + math.log10(1 - power) - 1.5 * log_2)
        if num_digits > denom_digits:
            count += 1
    return count
