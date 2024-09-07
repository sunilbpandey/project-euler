from itertools import combinations, permutations
from src.utils.py.prime import generate_primes, is_prime


def solve1() -> int:
    primes = generate_primes(10000)
    groups: dict[str, list[int]] = {}
    for prime in primes:
        if prime < 1000:
            continue

        key = "".join(sorted(list(str(prime))))
        groups.setdefault(key, []).append(prime)
        if len(groups[key]) >= 3 and key != "1478":
            for combination in combinations(groups[key], 3):
                # combinations returns tuples in sorted order according to the input
                # Since groups[key] is sorted in ascending order, by construction,
                # we know that combination will be sorted in ascending order as well
                if combination[1] - combination[0] == combination[2] - combination[1]:
                    return int("".join(str(n) for n in combination))
    raise RuntimeError("No solution found")


def solve() -> int:
    primes = generate_primes(10000)
    for prime in primes:
        if prime < 1000 or prime == 1487:
            continue

        # Generate all permutations of the digits
        candidates = [int("".join(perm)) for perm in permutations(str(prime))]

        # Filter out all permutations that are not prime or smaller than the original
        candidates = [c for c in candidates if c > prime and is_prime(c, primes)]

        for candidate in candidates:
            if candidate + candidate - prime in candidates:
                return int(f"{prime}{candidate}{candidate + candidate - prime}")
    raise RuntimeError("No solution found")
