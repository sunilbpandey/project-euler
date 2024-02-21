def solve() -> int:
    digit_sum = 0

    # pylint: disable=invalid-name
    for n in range(2, 100):
        a, b = 5 * n, 5
        prev = ""
        while True:
            if a >= b:
                a, b = a - b, b + 10
            else:
                a, b = a * 100, 10 * b - 45

            if a == 0:
                # perfect square
                break

            digits = str(b)
            if len(digits) >= 100:
                if prev == digits[:100]:
                    digit_sum += sum(int(d) for d in digits[:100])
                    break
                prev = digits[:100]
    # pylint: enable=invalid-name
    return int(digit_sum)
