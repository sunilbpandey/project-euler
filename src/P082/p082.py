import os


def solve() -> int:
    # pylint: disable=duplicate-code
    input_path = os.path.join(os.path.dirname(__file__), "0082_matrix.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    matrix = []
    for line in content.splitlines():
        matrix.append([int(n) for n in line.split(",")])
    # pylint: enable=duplicate-code

    size = len(matrix)
    cost = [[0] * size for _ in range(size)]
    for rownum, _ in enumerate(matrix):
        cost[rownum][1] = matrix[rownum][0] + matrix[rownum][1]

    for colnum in range(2, size):
        for rownum in range(size):
            all_path_sums = [cost[rownum][colnum - 1] + matrix[rownum][colnum]]

            # all paths from the top to the currrent row
            for start in range(rownum):
                path_sum = cost[start][colnum - 1] + matrix[rownum][colnum]
                for idx in range(start + 1, rownum + 1):
                    path_sum += matrix[idx][colnum - 1]
                all_path_sums.append(path_sum)

            # all paths from the row below the current row to the bottom
            for start in range(rownum + 1, size):
                path_sum = cost[start][colnum - 1] + matrix[rownum][colnum]
                for idx in range(rownum, start):
                    path_sum += matrix[idx][colnum - 1]
                all_path_sums.append(path_sum)

            cost[rownum][colnum] = min(all_path_sums)
    return min(row[-1] for row in cost)
