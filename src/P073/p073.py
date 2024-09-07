import math


def solve1() -> int:
    count = 0
    for denominator in range(4, 12001):
        start = denominator // 3
        end = (denominator - 1) // 2
        for num in range(start + 1, end + 1):
            if math.gcd(num, denominator) == 1:
                count += 1
    return count


def solve() -> int:
    count = 0
    stack = []
    left, right = 3, 2
    while True:
        mediant = left + right
        if mediant <= 12000:
            count += 1
            stack.append(right)
            right = mediant
            continue

        if not stack:
            break
        left, right = right, stack.pop()
    return count
