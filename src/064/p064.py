import math


def is_perfect_square(number: int) -> bool:
    root = int(math.floor(math.sqrt(number)))
    return number == root**2


# pylint: disable=invalid-name
def _get_next_term(n: int, p: int, q: int) -> tuple[int, int, int]:
    q = (n - p**2) // q
    m = int((math.sqrt(n) - p) // q)
    p = -p - m * q
    return (m, p, q)
    # pylint: enable=invalid-name


# pylint: disable=invalid-name
def _get_continued_faction_period(n: int) -> int:
    root = int(math.floor(math.sqrt(n)))
    seen: set[tuple[int, int, int]] = set()
    p, q = -root, 1
    while True:
        (m, p, q) = _get_next_term(n, p, q)
        if (m, p, q) in seen:
            return len(seen)
        seen.add((m, p, q))
    # pylint: enable=invalid-name


def solve() -> int:
    count = 1
    number = 2
    while number <= 10000:
        if is_perfect_square(number + 2):
            # n = m^2 - 2
            # so we can count m^2 + 1 as a solution and skip the next 5 numbers
            if number + 3 <= 10000:
                count += 1
            number += 5
            continue

        period = _get_continued_faction_period(number)
        if period % 2 == 1:
            count += 1
        number += 1
    return count
