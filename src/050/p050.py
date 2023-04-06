from src.utils.py.prime import generate_primes, is_prime


def solve() -> int:
    # By inspection, sum of prime numbers below 4000 more than one million
    primes = generate_primes(4000)

    max_term_count = 0
    max_term_count_prime = 0
    for start, total in enumerate(primes):
        for end in range(start + 1, len(primes)):
            total += primes[end]
            if total >= 1000000:
                break

            # Don't bother testing if the total is prime
            # if the number of terms is less than the current max
            if end - start + 1 > max_term_count and is_prime(total, primes):
                max_term_count = end - start + 1
                max_term_count_prime = total
    return max_term_count_prime
