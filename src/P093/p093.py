# pylint: disable=invalid-name
# pylint: disable=too-many-nested-blocks


def permutations(arr: list[int]) -> list[list[int]]:
    if len(arr) == 1:
        return [arr]

    perms: list[list[int]] = []
    for i, n in enumerate(arr):
        for p in permutations(arr[:i] + arr[i + 1 :]):
            perms.append([n] + p)
    return perms


def evaluate(items: list[int | str]) -> float:
    stack: list[float] = []
    for item in items:
        if isinstance(item, int):
            stack.append(item)
            continue
        b = stack.pop()
        a = stack.pop()
        match item:
            case "+":
                stack.append(a + b)
            case "-":
                stack.append(a - b)
            case "*":
                stack.append(a * b)
            case "/":
                if b == 0:
                    raise ValueError("division by zero")
                stack.append(a / b)
    return stack[0]


def make_numbers(a: int, b: int, c: int, d: int, numbers: list[bool]) -> None:
    ops = ["+", "-", "*", "/"]
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                patterns: list[list[int | str]] = [
                    [a, b, op1, c, op2, d, op3],
                    [a, b, c, op2, op1, d, op3],
                    [a, b, op1, c, d, op3, op2],
                    [a, b, c, op2, d, op3, op1],
                    [a, b, c, d, op3, op2, op1],
                ]
                for pat in patterns:
                    try:
                        result = evaluate(pat)
                        if result == int(result) and result > 0:
                            numbers[int(result)] = True
                    except ValueError:
                        pass


def solve() -> int:
    max_numbers = 0
    answer = ""
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    numbers = [False] * 3025
                    for a1, b1, c1, d1 in permutations([a, b, c, d]):
                        make_numbers(a1, b1, c1, d1, numbers)
                    for i in range(1, len(numbers)):
                        if not numbers[i]:
                            if i - 1 > max_numbers:
                                max_numbers = i - 1
                                answer = f"{a}{b}{c}{d}"
                            break
    return int(answer)
