import math
import os


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "0099_base_exp.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read().splitlines()

    max_log = 0.0
    linenum = 0
    for i, line in enumerate(content):
        base, exp = line.split(",")
        log = math.log(int(base)) * int(exp)
        if log > max_log:
            max_log = log
            linenum = i + 1
    return linenum
