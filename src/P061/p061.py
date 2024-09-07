from collections import defaultdict, namedtuple
from itertools import dropwhile, takewhile
from typing import Iterable
from src.utils.py.series import (
    pentagonal_numbers,
    triangle_numbers,
    hexagonal_numbers,
    hepagonal_numbers,
    octagonal_numbers,
    square_numbers,
)


FigurateNumber = namedtuple("FigurateNumber", ["type", "number"])


def find_cyclic_set(
    numbers: dict[int, list[FigurateNumber]],
    seen: list[FigurateNumber],
) -> list[int]:
    if len(seen) == 6:
        if seen[0].number // 100 == seen[-1].number % 100:
            return [num.number for num in seen]
        return []

    suffix = seen[-1].number % 100
    if suffix in numbers:
        for poly_type, num in numbers[suffix]:
            if poly_type in [num.type for num in seen]:
                continue
            cyclic_set = find_cyclic_set(
                numbers, seen + [FigurateNumber(poly_type, num)]
            )
            if cyclic_set:
                return cyclic_set
    return []


def four_digits_only(iterable: Iterable[int]) -> Iterable[int]:
    return takewhile(lambda n: n < 10000, dropwhile(lambda n: n < 1000, iterable))


def solve() -> int:
    # Map of two-digit prefix to list of figurate numbers starting with that prefix
    numbers: dict[int, list[FigurateNumber]] = defaultdict(list)

    # Populate the map with all four-digit figurate numbers up to heptagonal numbers
    generators = {
        3: triangle_numbers(),
        4: square_numbers(),
        5: pentagonal_numbers(),
        6: hexagonal_numbers(),
        7: hepagonal_numbers(),
    }
    for poly_type, generator in generators.items():
        for num in four_digits_only(generator):
            key = num // 100
            numbers[key].append(FigurateNumber(poly_type, num))

    # Since the set is cyclic, it doesn't matter which number we start with.
    # Start with octagonal numbers since there are fewer of them
    for num in four_digits_only(octagonal_numbers()):
        cyclic_set = find_cyclic_set(numbers, [FigurateNumber(8, num)])
        if cyclic_set:
            return sum(cyclic_set)
    raise RuntimeError("No solution found")
