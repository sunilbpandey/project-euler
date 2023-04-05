def solve1() -> int:
    total = 0
    for number in range(1, 1001):
        power = 1
        for _ in range(number):
            power = (power * number) % 10000000000
        total = (total + power) % 10000000000
    return total


def solve() -> int:
    return int(sum(i**i for i in range(1, 1001)) % 10000000000)
