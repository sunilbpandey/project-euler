import itertools
from src.utils.py.prime import generate_primes, is_prime


def is_sum_of_prime_and_twice_a_square(
    number: int, primes: list[int], double_squares: list[int]
) -> bool:
    # Check if there is any double square that when subtracted from the number
    # yields a prime number
    filtered = itertools.takewhile(lambda dsq: dsq <= number, double_squares)
    return any(is_prime(number - dsq, primes) for dsq in filtered)


def solve() -> int:
    # Assume there is a solution below 1 million
    double_squares = [2 * i * i for i in range(1, 1000)]
    primes = generate_primes(1000)
    for number in itertools.count(start=9, step=2):
        if not is_prime(number, primes):
            if not is_sum_of_prime_and_twice_a_square(number, primes, double_squares):
                return number
    raise RuntimeError("No solution found")
