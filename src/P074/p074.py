import math

FACTORIALS = [math.factorial(i) for i in range(10)]


def digit_factorial_sum(num: int) -> int:
    return sum(FACTORIALS[int(digit)] for digit in str(num))


def sort_digits(num: int) -> int:
    return int("".join(sorted(str(num).replace("0", "1"))))


def solve() -> int:
    chain_lengths = [0] * 3000001

    # preset the chain lengths of known loops
    for num in (1, 2, 145, 40585):
        chain_lengths[num] = 1
    for num in (871, 45361, 872, 45362):
        chain_lengths[num] = 2
    for num in (169, 363601, 1454):
        chain_lengths[num] = 3

    for num in range(1, 1000001):
        if chain_lengths[num]:
            continue

        num_hash = sort_digits(num)
        if chain_lengths[num_hash]:
            chain_lengths[num] = chain_lengths[num_hash]
            continue

        chain = []
        while not chain_lengths[num]:
            chain.append(num)
            num = digit_factorial_sum(num)

        # pylint: disable=invalid-name
        for i, n in enumerate(chain):
            if chain_lengths[n] == 0:
                chain_lengths[n] = len(chain) + chain_lengths[num] - i
        # pylint: enable=invalid-name
    return sum(1 for n in chain_lengths if n == 60)
