import itertools


def solve() -> int:
    total = 0
    for number in itertools.permutations(range(10)):
        if number[0] == 0:
            continue
        if number[3] % 2 != 0:
            continue
        if number[5] % 5 != 0:
            continue
        if (number[2] + number[3] + number[4]) % 3 != 0:
            continue
        if (number[4] * 100 + number[5] * 10 + number[6]) % 7 != 0:
            continue
        if (number[5] * 100 + number[6] * 10 + number[7]) % 11 != 0:
            continue
        if (number[6] * 100 + number[7] * 10 + number[8]) % 13 != 0:
            continue
        if (number[7] * 100 + number[8] * 10 + number[9]) % 17 != 0:
            continue
        total += int("".join(str(d) for d in number))
    return total
