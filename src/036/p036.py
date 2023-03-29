from collections.abc import Generator
import itertools


def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


def parse_binary(bits: list[int]) -> int:
    return int("".join(str(d) for d in bits), base=2)


def binary_palindromes(length: int) -> Generator[int, None, None]:
    # To generate a binary palindrome of length n, generate the (n - 2) / 2 middle bits.
    # If n is even, reverse the middle bits and concatenate them.
    # If n is odd, reverse the middle bits and concatenate them, excluding the last bit.
    for bits in [list(p) for p in itertools.product([0, 1], repeat=(length - 1) // 2)]:
        if length % 2 == 0:
            yield parse_binary([1] + bits + bits[::-1] + [1])
        else:
            yield parse_binary([1] + bits[:-1] + bits[::-1] + [1])


def solve() -> int:
    # This can be compressed into a one-liner, but I think this is more readable.
    total = 1  # 1 is a palindrome
    for length in range(2, 21):
        total += sum(n for n in binary_palindromes(length) if is_palindrome(n))
    return total
