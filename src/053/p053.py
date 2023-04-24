import math


def solve1() -> int:
    total = 0
    # pylint: disable=invalid-name
    for n in range(23, 101):
        for r in range(n):
            if math.comb(n, r) > 1000000:
                total += 1
    # pylint: enable=invalid-name
    return total


def solve2() -> int:
    total = 0
    # pylint: disable=invalid-name
    for n in range(23, 101):
        r = next(r for r in range(4, n - 3) if math.comb(n, r) > 1000000)
        total += n - 2 * r + 1
    # pylint: enable=invalid-name
    return total


def solve() -> int:
    total = 0
    row: list[int] = []
    # pylint: disable=invalid-name
    for n in range(101):
        row.insert(0, 1)
        for i in range(1, len(row) - 1):
            row[i] += row[i + 1]
            if row[i] > 1000000:
                total += n - 2 * i + 1

                # no need to keep the rest of the list in memory
                del row[i + 1 :]
                break
    # pylint: enable=invalid-name
    return total
