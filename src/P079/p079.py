import os


__visited: set[str] = set()
__edges: dict[str, set[str]] = {}


def visit(node: str, answer: str) -> str:
    if node in __visited:
        return answer

    for dest in __edges.get(node, set()):
        answer = visit(dest, answer)

    __visited.add(node)
    return node + answer


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "keylog.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()
    guesses = content.splitlines()

    nodes = set()
    for guess in guesses:
        for i in range(3):
            nodes.add(guess[i])
            __edges.setdefault(guess[i], set())
            for j in range(i + 1, 3):
                __edges[guess[i]].add(guess[j])

    answer = ""
    while nodes:
        answer = visit(nodes.pop(), answer)
    return int(answer)
