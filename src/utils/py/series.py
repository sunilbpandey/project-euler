from collections.abc import Generator


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
