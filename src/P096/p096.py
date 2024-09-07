# pylint: disable=invalid-name
import copy
import os


def get_candidates(value: str) -> str:
    return value if value != "0" else "123456789"


def init(puzzle: list[str]) -> list[list[str]]:
    return [[get_candidates(puzzle[i][j]) for j in range(9)] for i in range(9)]


def remove_at(grid: list[list[str]], row: int, col: int, digit: str) -> None:
    grid[row][col] = grid[row][col].replace(digit, "")


def remove_from_row(grid: list[list[str]], row: int, col: int) -> bool:
    removed = False
    digit = grid[row][col]
    for index in range(9):
        if index != col and digit in grid[row][index]:
            remove_at(grid, row, index, digit)
            removed = True
    return removed


def remove_from_col(grid: list[list[str]], row: int, col: int) -> bool:
    removed = False
    digit = grid[row][col]
    for index in range(9):
        if index != row and digit in grid[index][col]:
            remove_at(grid, index, col, digit)
            removed = True
    return removed


def remove_from_box(grid: list[list[str]], row: int, col: int) -> bool:
    removed = False
    digit = grid[row][col]
    for i in range(3):
        for j in range(3):
            r = row - row % 3 + i
            c = col - col % 3 + j
            if r != row and c != col and digit in grid[r][c]:
                remove_at(grid, r, c, digit)
                removed = True
    return removed


def solve_sudoku(grid: list[list[str]]) -> int:
    # if a cell has only one candidate digit,
    # remove that digit from other cells in the same row, column, and box
    while True:
        changed = False
        for i in range(9):
            for j in range(9):
                if len(grid[i][j]) > 1:
                    continue
                if len(grid[i][j]) == 0:
                    return 0
                digit = grid[i][j]
                remove_from_row(grid, i, j)
                remove_from_col(grid, i, j)
                remove_from_box(grid, i, j)
        if not changed:
            break

    # find the unsolved cell with fewest candidates
    unsolved = [(i, j) for i in range(9) for j in range(9) if len(grid[i][j]) > 1]
    if not unsolved:
        return int(grid[0][0] + grid[0][1] + grid[0][2])

    r, c = min(unsolved, key=lambda x: len(grid[x[0]][x[1]]))
    for digit in grid[r][c]:
        grid_copy = copy.deepcopy(grid)
        grid_copy[r][c] = digit
        solution = solve_sudoku(grid_copy)
        if solution > 0:
            return solution
    return 0


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "p096_sudoku.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    lines = content.splitlines()
    return sum(
        solve_sudoku(init(lines[i + 1 : i + 10])) for i in range(0, len(lines), 10)
    )
