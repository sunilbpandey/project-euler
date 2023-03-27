def solve() -> int:
    # First layer is a special case since it has only one number
    return sum(16 * n * n + 4 * n + 4 for n in range(1, 501)) + 1
