def solve() -> int:
    num = 28433
    for _ in range(7830457):
        num = (2 * num) % 10**10
    return num + 1
