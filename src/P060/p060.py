from src.utils.py.prime import generate_primes, is_prime


# Cache of primes to avoid testing them again
cache: dict[int, bool] = {}


def is_prime_cached(num: int, primes: list[int]) -> bool:
    if num not in cache:
        cache[num] = is_prime(num, primes)
    return cache[num]


def is_prime_pair(prime1: int, prime2: int, primes: list[int]) -> bool:
    if not is_prime_cached(int(str(prime1) + str(prime2)), primes):
        return False
    return is_prime_cached(int(str(prime2) + str(prime1)), primes)


def find_prime_set(candidates: list[int], primes: list[int]) -> list[int]:
    # pylint: disable=invalid-name, too-many-nested-blocks
    for i1, p1 in enumerate(candidates):
        for i2 in range(i1 + 1, len(candidates)):
            p2 = candidates[i2]
            if not is_prime_pair(p1, p2, primes):
                continue
            for i3 in range(i2 + 1, len(candidates)):
                p3 = candidates[i3]
                if any(not is_prime_pair(p, p3, primes) for p in [p1, p2]):
                    continue
                for i4 in range(i3 + 1, len(candidates)):
                    p4 = candidates[i4]
                    if any(not is_prime_pair(p, p4, primes) for p in [p1, p2, p3]):
                        continue
                    for i5 in range(i4 + 1, len(candidates)):
                        p5 = candidates[i5]
                        if all(is_prime_pair(p, p5, primes) for p in [p1, p2, p3, p4]):
                            return [p1, p2, p3, p4, p5]
    # pylint: enable=invalid-name, too-many-nested-blocks
    return []


def solve() -> int:
    # Limits of 10000 and 8400 are based on inspection
    # to make sure the program finishes quickly
    primes = generate_primes(10000)

    candidates = [3] + [p for p in primes if 5 < p < 8400 and p % 3 == 1]
    prime_set = find_prime_set(candidates, primes)
    if not prime_set:
        candidates = [3] + [p for p in primes if 5 < p < 8400 and p % 3 == 2]
        prime_set = find_prime_set(candidates, primes)
    return sum(prime_set)
