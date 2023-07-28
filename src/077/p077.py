from src.utils.py.prime import generate_primes


def solve() -> int:
    primes = generate_primes(100)
    limit = 100
    ways = [1] + [0] * limit
    for num in primes:
        for target in range(num, limit):
            ways[target] += ways[target - num]
        if ways[num] > 5000:
            return num
    raise RuntimeError("No solution found")
