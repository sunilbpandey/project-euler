import itertools


def solve() -> int:
    for base in itertools.count(start=2):
        limit = 10 ** (base + 1)
        for num in itertools.count(start=10**base):
            if num % 3 != 0:
                continue
            if num * 6 >= limit:
                break
            digits = sorted(str(num))
            if "0" not in digits and "5" not in digits:
                continue
            if "2" not in digits and "3" not in digits:
                continue
            if "3" not in digits and "4" not in digits:
                continue
            if "4" not in digits and "5" not in digits:
                continue
            if "5" not in digits and "6" not in digits:
                continue
            if "6" not in digits and "7" not in digits:
                continue
            if all(sorted(str(num * i)) == digits for i in range(2, 7)):
                return int(num)
    raise RuntimeError("No solution found")
