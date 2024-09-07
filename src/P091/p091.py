# pylint: disable=invalid-name
import math


def solve1() -> int:
    square = {x: x**2 for x in range(51)}
    count = 0
    for x1 in range(51):
        for y1 in range(1, 51):
            for x2 in range(x1, 51):
                for y2 in range(y1 + 1):
                    if (x1, y1) == (x2, y2) or (x2, y2) == (0, 0):
                        continue
                    asq = square[x2 - x1] + square[y1 - y2]
                    bsq = square[x2] + square[y2]
                    csq = square[x1] + square[y1]
                    if asq + bsq == csq or asq + csq == bsq or bsq + csq == asq:
                        count += 1
    return count


def solve() -> int:
    count = 0
    for x1 in range(1, 51):
        for y1 in range(1, 51):
            g = math.gcd(x1, y1)
            dx, dy = y1 // g, x1 // g
            count += min((50 - x1) // dx, y1 // dy)
    return 2 * count + 3 * 2500
