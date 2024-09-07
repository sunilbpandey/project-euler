def is_valid_solution(solution: list[int]) -> bool:
    return all(sum(solution[i : i + 3]) == sum(solution[0:3]) for i in range(3, 15, 3))


def find_maximum_solution(solution: list[int]) -> str:
    # find the first entry that is 0
    try:
        index = solution.index(0)
    except ValueError:
        if is_valid_solution(solution):
            return "".join(str(digit) for digit in solution)
        return ""

    candidates: list[int] = []
    repeat_index = index

    if index % 3 == 0:
        # external node
        candidates = [n for n in range(6, 11) if n not in solution]
    elif index % 3 == 1:
        # internal node
        candidates = [n for n in range(1, 6) if n not in solution]
        repeat_index = (index + 13) % 15
    else:
        # internal node
        candidates = [n for n in range(1, 6) if n not in solution]
        repeat_index = (index + 2) % 15

    solutions: list[str] = []
    for number in candidates:
        solution = solution[:]
        solution[index] = number
        solution[repeat_index] = number
        solutions.append(find_maximum_solution(solution))
    return max(solutions, default="")


def solve() -> int:
    solution = [6] + [0] * 14
    return int(find_maximum_solution(solution))
