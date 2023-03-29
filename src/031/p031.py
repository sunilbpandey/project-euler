COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def solve1() -> int:
    def count_ways(target: int, index: int) -> int:
        if index <= 0:
            return 1

        limit = target // COINS[index] + 1
        return sum(
            count_ways(target - i * COINS[index], index - 1) for i in range(limit)
        )

    return count_ways(200, len(COINS) - 1)


def solve2() -> int:
    def count_ways(target: int, index: int) -> int:
        if target == 0:
            return 1
        if target < 0 or index < 0:
            return 0
        return count_ways(target - COINS[index], index) + count_ways(target, index - 1)

    return count_ways(200, len(COINS) - 1)


def solve() -> int:
    amount = 200
    ways = [1] + [0] * amount
    for coin in COINS:
        for target in range(coin, amount + 1):
            ways[target] += ways[target - coin]
    return ways[amount]
