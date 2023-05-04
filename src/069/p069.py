from src.utils.py.prime import generate_primes, factorize


def totient(num: int, primes: list[int]) -> int:
    factors = factorize(num, primes)
    for factor in factors:
        num = (num * (factor - 1)) // factor
    return int(num)


def solve1() -> int:
    primes = generate_primes(1000)
    max_n = 0
    max_n_phi_n = 0.0
    for i in range(2, 1000001):
        n_phi_n = i / totient(i, primes)
        if n_phi_n > max_n_phi_n:
            max_n_phi_n = n_phi_n
            max_n = i
    return max_n


def solve() -> int:
    product = 1
    for prime in generate_primes(100):
        if prime * product > 1000000:
            break
        product *= prime
    return product
