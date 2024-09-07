from src.utils.py.math import totient
from src.utils.py.prime import generate_primes


def solve1() -> int:
    primes = generate_primes(1000)
    return sum(totient(d, primes) for d in range(2, 1000001))


def solve() -> int:
    totients = [0] * 1000001

    primes: list[int] = []
    for num in range(2, 1000001):
        if totients[num] == 0:
            totients[num] = num - 1
            primes.append(num)

        for prime in primes:
            if num * prime > 1000000:
                break
            multiplier = prime if num % prime == 0 else prime - 1
            totients[num * prime] = totients[num] * multiplier
    return sum(totients[2:])
