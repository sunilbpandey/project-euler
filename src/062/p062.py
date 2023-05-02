from collections import defaultdict
import itertools


def solve() -> int:
    cubes: dict[str, list[int]] = defaultdict(list)
    for i in itertools.count(1):
        cube = i**3
        key = "".join(sorted(str(cube)))
        cubes[key].append(cube)
        if len(cubes[key]) == 5:
            return cubes[key][0]
    raise RuntimeError("No solution found")
