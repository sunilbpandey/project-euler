def solve() -> int:
    largest_palindrome = 0

    # pylint: disable=invalid-name
    for b in range(10):
        for c in range(10):
            n = 10010 * b + 1100 * c + 900009
            for d in range(949, 1000, 2):
                if d % 5 == 0:
                    continue
                if n > largest_palindrome and n % d == 0:
                    m = n // d
                    if 100 <= m < 1000:
                        largest_palindrome = n
    # pylint: enable=invalid-name
    return largest_palindrome
