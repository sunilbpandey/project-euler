import itertools
from src.utils.py.prime import generate_primes, is_prime


def is_circle_prime(digits: tuple[int, ...], primes: list[int]) -> bool:
    digit_str = "".join(str(d) for d in digits)
    for _ in range(len(digits)):
        if not is_prime(int(digit_str), primes):
            return False
        digit_str = digit_str[1:] + digit_str[0]
    return True


def solve() -> int:
    primes = generate_primes(1000)

    # Count single-digit primes separately
    count = len(list(itertools.takewhile(lambda n: n < 10, primes)))

    for length in range(2, 7):
        for combo in itertools.product([1, 3, 7, 9], repeat=length):
            if is_circle_prime(combo, primes):
                count += 1
    return count
