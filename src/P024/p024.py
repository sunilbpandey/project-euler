import math


def solve() -> int:
    answer = ""
    digits = list(range(10))

    permutations = 1000000 - 1
    while len(digits) > 0:
        factorial = math.factorial(len(digits) - 1)
        answer += str(digits.pop(permutations // factorial))
        permutations %= factorial
    return int(answer)
