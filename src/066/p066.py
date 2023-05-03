from src.utils.py.series import convergents, is_perfect_square, sqrt_continued_fraction


def solve() -> int:
    max_x = 0
    max_d = 0
    for d in range(2, 1001):  # pylint: disable=invalid-name
        if is_perfect_square(d):
            continue

        # pylint: disable=invalid-name
        for h, k in convergents(sqrt_continued_fraction(d)):
            if h**2 - d * k**2 == 1:
                if h > max_x:
                    max_x = h
                    max_d = d
                break
        # pylint: enable=invalid-name
    return max_d
