coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count_ways(total: int, index: int) -> int:
    if index <= 0:
        return 1

    limit = total // coins[index] + 1
    return sum(count_ways(total - i * coins[index], index - 1) for i in range(limit))


def solve() -> int:
    return count_ways(200, len(coins) - 1)
