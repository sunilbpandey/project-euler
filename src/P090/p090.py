import itertools


def is_valid(cube1: str, cube2: str) -> bool:
    upsidedown = {"6": "9", "9": "6"}
    for key, val in upsidedown.items():
        if key in cube1 and val not in cube1:
            cube1 += val
        if key in cube2 and val not in cube2:
            cube2 += val

    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
    return all(
        (s[0] in cube1 and s[1] in cube2) or (s[0] in cube2 and s[1] in cube1)
        for s in squares
    )


def generate(cube1: str, cube2: str, digits: list[str]) -> set[tuple[str, str]]:
    if len(cube1) == 6 and len(cube2) == 6:
        if not is_valid(cube1, cube2):
            return set()
        cube1 = "".join(sorted(cube1))
        cube2 = "".join(sorted(cube2))
        if cube2 < cube1:
            cube1, cube2 = cube2, cube1
        return {(cube1, cube2)}

    if len(digits) == 0:
        return set()
    digit = digits[0]

    # digit can be in both the cubes, or exactly one of them, or neither of them
    cube1copy = cube1 + digit if len(cube1) < 6 else cube1
    cube2copy = cube2 + digit if len(cube2) < 6 else cube2

    arrangements = set()
    arrangements.update(generate(cube1copy, cube2copy, digits[1:]))
    arrangements.update(generate(cube1copy, cube2, digits[1:]))
    arrangements.update(generate(cube1, cube2copy, digits[1:]))
    arrangements.update(generate(cube1, cube2, digits[1:]))
    return arrangements


def solve1() -> int:
    return len(generate("", "", [str(i) for i in range(10)]))


def solve() -> int:
    cubes = ["".join(sorted(c)) for c in itertools.combinations("0123456789", 6)]
    return sum(
        1 for cube1, cube2 in itertools.combinations(cubes, 2) if is_valid(cube1, cube2)
    )
