from collections.abc import Generator, Iterable
import itertools
import math


def fibonacci(
    a: int = 1, b: int = 1  # pylint: disable=invalid-name
) -> Generator[int, None, None]:
    while True:
        yield a
        a, b = b, a + b


def figurate_numbers(step: int) -> Generator[int, None, None]:
    difference = 1
    number = 0
    while True:
        number += difference
        yield number
        difference += step


def triangle_numbers() -> Generator[int, None, None]:
    return figurate_numbers(1)


def square_numbers() -> Generator[int, None, None]:
    return figurate_numbers(2)


def pentagonal_numbers() -> Generator[int, None, None]:
    return figurate_numbers(3)


def hexagonal_numbers() -> Generator[int, None, None]:
    return figurate_numbers(4)


def hepagonal_numbers() -> Generator[int, None, None]:
    return figurate_numbers(5)


def octagonal_numbers() -> Generator[int, None, None]:
    return figurate_numbers(6)


def is_perfect_square(number: int) -> bool:
    root = int(math.floor(math.sqrt(number)))
    return number == root**2


def e_continued_fraction() -> Generator[int, None, None]:
    yield 2
    for k in itertools.count(1):
        yield 1
        yield 2 * k
        yield 1


def sqrt_continued_fraction(number: int) -> Generator[int, None, None]:
    sqrt = math.sqrt(number)
    root = int(math.floor(sqrt))
    yield root

    p, q = -root, 1  # pylint: disable=invalid-name
    while True:
        q = (number - p**2) // q
        m = int((sqrt - p) // q)  # pylint: disable=invalid-name
        p = -p - m * q
        yield m


def convergents(
    continued_fraction: Iterable[int],
) -> Generator[tuple[int, int], None, None]:
    h0, h1 = 0, 1
    k0, k1 = 1, 0
    for a in continued_fraction:
        h = a * h1 + h0
        k = a * k1 + k0
        yield (h, k)
        h0, h1 = h1, h
        k0, k1 = k1, k
