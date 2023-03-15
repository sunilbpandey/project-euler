from itertools import combinations


def solve1() -> int:
    n = 100  # pylint: disable=invalid-name
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    return square_of_sum - sum_of_squares


def solve() -> int:
    return 2 * sum(i * j for i, j in combinations(range(1, 101), 2))
