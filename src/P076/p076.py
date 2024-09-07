def solve() -> int:
    amount = 100
    ways = [1] + [0] * amount
    for num in range(1, amount):
        for target in range(num, amount + 1):
            ways[target] += ways[target - num]
    return ways[amount]
