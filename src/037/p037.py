import itertools
from src.utils.py.prime import generate_primes, is_prime


def is_left_truncatable(digits: tuple[int, ...], primes: list[int]) -> bool:
    string = "".join(str(d) for d in digits)
    for i in range(len(digits)):
        if not is_prime(int(string[i:]), primes=primes):
            return False
    return True


def is_right_truncatable(digits: tuple[int, ...], primes: list[int]) -> bool:
    string = "".join(str(d) for d in digits)
    for i in range(len(digits)):
        if not is_prime(int(string[: i + 1]), primes=primes):
            return False
    return True


def solve() -> int:
    primes = generate_primes(1000)
    truncatable_primes: list[int] = []
    for length in itertools.count():
        if len(truncatable_primes) == 11:
            break

        middle_digits = itertools.tee([1, 3, 7, 9], length)
        for combo in itertools.product([1, 2, 3, 5, 7, 9], *middle_digits, [3, 7]):
            if is_left_truncatable(combo, primes=primes) and is_right_truncatable(
                combo, primes=primes
            ):
                truncatable_primes.append(int("".join(str(d) for d in combo)))
    return sum(truncatable_primes)
