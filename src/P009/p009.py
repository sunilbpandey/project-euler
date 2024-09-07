def solve() -> int:
    # pylint: disable=invalid-name
    for m in range(1, 22):
        for n in range(1, m):
            if m * (m + n) == 500:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                return a * b * c
    # pylint: enable=invalid-name

    raise Exception("No solution found")  # pylint: disable=broad-exception-raised
