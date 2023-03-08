from typing import Generator
import itertools


def fibonacci(
    a: int = 1, b: int = 1  # pylint: disable=invalid-name
) -> Generator[int, None, None]:
    while True:
        yield a
        a, b = b, a + b


def solve() -> int:
    return sum(
        n for n in itertools.takewhile(lambda n: n < 4000000, fibonacci()) if n % 2 == 0
    )
