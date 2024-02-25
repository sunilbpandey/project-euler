# pylint: disable=duplicate-code
# pylint: disable=invalid-name
from typing import cast
import os


def find_next_unvisited(
    visited: list[list[bool]], path_sums: list[list[int | None]]
) -> tuple[int, int]:
    min_path_sum = None
    min_r = -1
    min_c = -1
    size = len(visited)

    for r in range(size):
        for c in range(size):
            if (
                not visited[r][c]
                and path_sums[r][c] is not None
                and (min_path_sum is None or path_sums[r][c] < min_path_sum)
            ):
                min_path_sum = path_sums[r][c]
                min_r, min_c = r, c
    return min_r, min_c


def min_value(a: int | None, b: int) -> int:
    if a is None:
        return b
    return a if a < b else b


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "0083_matrix.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    matrix = []
    for line in content.splitlines():
        matrix.append([int(n) for n in line.split(",")])

    size = len(matrix)
    visited = [[False] * size for _ in matrix]
    path_sums: list[list[int | None]] = [[None] * size for _ in matrix]
    path_sums[0][0] = matrix[0][0]

    r, c = 0, 0
    while True:
        r, c = find_next_unvisited(visited, path_sums)
        path_sum_so_far = cast(int, path_sums[r][c])
        if r > 0 and not visited[r - 1][c]:
            path_sums[r - 1][c] = min_value(
                path_sums[r - 1][c], path_sum_so_far + matrix[r - 1][c]
            )

        if r < size - 1 and not visited[r + 1][c]:
            path_sums[r + 1][c] = min_value(
                path_sums[r + 1][c], path_sum_so_far + matrix[r + 1][c]
            )

        if c > 0 and not visited[r][c - 1]:
            path_sums[r][c - 1] = min_value(
                path_sums[r][c - 1], path_sum_so_far + matrix[r][c - 1]
            )

        if c < size - 1 and not visited[r][c + 1]:
            path_sums[r][c + 1] = min_value(
                path_sums[r][c + 1], path_sum_so_far + matrix[r][c + 1]
            )
        visited[r][c] = True

        if r == size - 1 and c == size - 1:
            break
    return cast(int, path_sums[size - 1][size - 1])
