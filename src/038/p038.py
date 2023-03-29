from collections.abc import Generator


def pandigital_concatenated_products() -> Generator[int, None, None]:
    for number in range(999, 10000):
        digits = str(number) + str(number * 2)
        if "".join(sorted(digits)) == "123456789":
            yield int(digits)


def solve() -> int:
    return max(pandigital_concatenated_products())
