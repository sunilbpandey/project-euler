def solve() -> int:
    largest = 0
    for number in range(999, 10000):
        digits = str(number) + str(number * 2)
        if "".join(sorted(digits)) == "123456789":
            largest = max(largest, int(digits))
    return largest
