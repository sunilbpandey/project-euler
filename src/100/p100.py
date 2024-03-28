# pylint: disable=invalid-name
def solve() -> int:
    r0, r1, b1 = 1, 6, 15
    while b1 + r1 <= 10**12:
        r2 = 6 * r1 - r0
        b1 = (r2 - r1 + 1) // 2
        r0, r1 = r1, r2
    return b1
