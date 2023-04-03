from src.utils.py.series import pentagonal_numbers


def solve() -> int:
    pentagonals: set[int] = set()
    for curr in pentagonal_numbers():
        for prev in pentagonals:
            if curr - prev in pentagonals and curr - 2 * prev in pentagonals:
                return curr - 2 * prev
        pentagonals.add(curr)
    raise RuntimeError("No solution found")
