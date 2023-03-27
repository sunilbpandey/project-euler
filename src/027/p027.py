from src.utils.py.prime import generate_primes, is_prime


def solve() -> int:
    primes = generate_primes(1415)
    max_consecutive_primes = 0
    product = 0
    for a in range(-999, 1000):  # pylint: disable=invalid-name
        for b in range(3, 1000, 2):  # pylint: disable=invalid-name
            count = 0
            for n in range(0, b):  # pylint: disable=invalid-name
                number = n * n + a * n + b
                if number < 0 or not is_prime(number, primes):
                    break
                count += 1
            if count > max_consecutive_primes:
                max_consecutive_primes = count
                product = a * b
    return product
