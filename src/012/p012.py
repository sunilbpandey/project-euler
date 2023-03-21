from src.utils.py.math import count_of_divisors
from src.utils.py.prime import generate_primes, factorize
from src.utils.py.series import triangle_numbers


def solve() -> int:
    primes = generate_primes(9000)
    for triangle in triangle_numbers():
        factors = factorize(triangle, primes=primes)
        if count_of_divisors(triangle, factors=factors) > 500:
            return triangle
    raise Exception("No solution found")  # pylint: disable=broad-exception-raised
