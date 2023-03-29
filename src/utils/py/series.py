from collections.abc import Generator


def fibonacci(
    a: int = 1, b: int = 1  # pylint: disable=invalid-name
) -> Generator[int, None, None]:
    while True:
        yield a
        a, b = b, a + b


def triangle_numbers() -> Generator[int, None, None]:
    n = 1
    triangle = 0
    while True:
        triangle += n
        yield triangle
        n += 1
