import math
from src.utils.py.prime import generate_primes
from src.utils.py.math import totient


def solve1() -> int:
    primes = generate_primes(3200)
    min_n = 0
    min_n_phi_n = math.inf
    for number in range(2, 10000001):
        phi_n = totient(number, primes)
        if sorted(str(number)) == sorted(str(phi_n)):
            n_phi_n = number / phi_n
            if n_phi_n < min_n_phi_n:
                min_n_phi_n = n_phi_n
                min_n = number
    return min_n


def solve() -> int:
    primes = generate_primes(5000)
    min_n = 0
    min_n_phi_n = math.inf
    for i, p1 in enumerate(primes):  # pylint: disable=invalid-name
        if p1 < 2000:
            continue
        if p1 > 3162:
            break

        for j in range(i + 1, len(primes)):
            n = p1 * primes[j]  # pylint: disable=invalid-name
            if n > 10000000:
                break

            phi_n = (p1 - 1) * (primes[j] - 1)
            if sorted(str(n)) != sorted(str(phi_n)):
                continue

            n_phi_n = n / phi_n
            if n_phi_n < min_n_phi_n:
                min_n_phi_n = n_phi_n
                min_n = n
    return min_n
