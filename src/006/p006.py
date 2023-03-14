def solve() -> int:
    n = 100  # pylint: disable=invalid-name
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    return square_of_sum - sum_of_squares
