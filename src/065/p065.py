import math


def solve1() -> int:
    term = 100
    num = 3 if term % 3 == 0 else 1
    den = 2 * term if term % 3 == 0 else 1

    for i in range(term - 1, 1, -1):
        if i % 3 == 0:
            # add 2*i/3 to the fraction
            num += 2 * (i // 3) * den
        else:
            # add 1 to the fraction
            num += den
        num, den = den, num
    num += 2 * den

    # simplify the fraction
    gcd = math.gcd(num, den)
    num, den = num // gcd, den // gcd
    return sum(int(digit) for digit in str(num))


def solve() -> int:
    num1, num2 = 2, 3
    # pylint: disable=invalid-name
    for k in range(3, 101):
        a = 2 * (k // 3) if k % 3 == 0 else 1
        num1, num2 = num2, a * num2 + num1
    # pylint: enable=invalid-name
    return sum(int(digit) for digit in str(num2))
