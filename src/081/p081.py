import os


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "0081_matrix.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    matrix = []
    for line in content.splitlines():
        matrix.append([int(n) for n in line.split(",")])

    size = len(matrix)
    path_sums = [[0] * size for _ in range(size)]
    for row in range(size):  # pylint: disable=consider-using-enumerate
        for col in range(size):
            neighbours = []
            if row > 0:
                neighbours.append(path_sums[row - 1][col])
            if col > 0:
                neighbours.append(path_sums[row][col - 1])

            min_neighbour = min(neighbours) if neighbours else 0
            path_sums[row][col] = matrix[row][col] + min_neighbour

    return path_sums[size - 1][size - 1]
