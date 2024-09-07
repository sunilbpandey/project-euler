# pylint: disable=invalid-name
import math
from src.utils.py.prime import generate_primes


def solve() -> int:
    limit = 50 * 1000 * 1000
    primes = generate_primes(math.floor(math.sqrt(limit)) + 1)

    pow2 = []
    pow3 = []
    pow4 = []
    for p in primes:
        if p**2 < limit:
            pow2.append(p**2)
        if p**3 < limit:
            pow3.append(p**3)
        if p**4 < limit:
            pow4.append(p**4)

    return len(
        {a + b + c for a in pow2 for b in pow3 for c in pow4 if a + b + c < limit}
    )
