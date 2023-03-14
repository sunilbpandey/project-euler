def gcd(a: int, b: int) -> int:  # pylint: disable=invalid-name
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def lcm(a: int, b: int) -> int:  # pylint: disable=invalid-name
    return a * (b // gcd(a, b))
