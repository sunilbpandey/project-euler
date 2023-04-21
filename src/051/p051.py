import itertools
from src.utils.py.prime import is_prime


def generate_family(num: str, mask: tuple[int, int, int]) -> list[str]:
    family: list[str] = []
    digits = range(1, 10) if 0 in mask else range(10)
    for digit in digits:
        family.append(
            "".join(str(digit) if i in mask else n for i, n in enumerate(num))
        )
    return family


def generate_prime_family(num: str, primes: list[int]) -> list[str]:
    family: list[str] = []
    for indices in itertools.combinations(range(len(num) - 1), 3):
        if num[indices[0]] == num[indices[1]] == num[indices[2]]:
            candidates = generate_family(num, indices)
            for candidate in candidates:
                if is_prime(int(candidate), primes):
                    family.append(candidate)
    return family


def solve() -> int:
    sieve: dict[int, list[int]] = {}
    primes: list[int] = []

    # pylint: disable=duplicate-code
    for num in itertools.count(start=2):
        if num in sieve:
            # num is composite and sieve[num] contains its prime factors
            factors = sieve[num]
            del sieve[num]
        else:
            # num is prime
            factors = [num]
            primes.append(num)
            family = generate_prime_family(str(num), primes)
            if len(family) == 8:
                return num

        # Mark next multiple of each factor
        for prime in factors:
            sieve.setdefault(num + prime, []).append(prime)
    # pylint: enable=duplicate-code
    raise RuntimeError("No solution found")
