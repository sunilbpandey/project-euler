import os


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "p067_triangle.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    triangle = [[int(n) for n in line.split()] for line in content.split("\n") if line]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]
