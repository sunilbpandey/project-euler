import importlib
import pytest

SOLUTIONS = [
    {"problem": 1, "solution": "233168"},
    {"problem": 2, "solution": "4613732"},
    {"problem": 3, "solution": "6857"},
    {"problem": 4, "solution": "906609"},
    {"problem": 5, "solution": "232792560"},
    {"problem": 6, "solution": "25164150"},
    {"problem": 7, "solution": "104743"},
    {"problem": 8, "solution": "23514624000"},
    {"problem": 9, "solution": "31875000"},
    {"problem": 10, "solution": "142913828922"},
    {"problem": 11, "solution": "70600674"},
    {"problem": 12, "solution": "76576500"},
    {"problem": 13, "solution": "5537376230"},
    {"problem": 14, "solution": "837799"},
    {"problem": 15, "solution": "137846528820"},
    {"problem": 16, "solution": "1366"},
    {"problem": 17, "solution": "21124"},
    {"problem": 18, "solution": "1074"},
    {"problem": 19, "solution": "171"},
    {"problem": 20, "solution": "648"},
    {"problem": 21, "solution": "31626"},
    {"problem": 22, "solution": "871198282"},
    {"problem": 23, "solution": "4179871"},
    {"problem": 24, "solution": "2783915460"},
    {"problem": 25, "solution": "4782"},
    {"problem": 26, "solution": "983"},
    {"problem": 27, "solution": "-59231"},
    {"problem": 28, "solution": "669171001"},
    {"problem": 29, "solution": "9183"},
    {"problem": 30, "solution": "443839"},
    {"problem": 31, "solution": "73682"},
    {"problem": 32, "solution": "45228"},
    {"problem": 33, "solution": "100"},
    {"problem": 34, "solution": "40730"},
    {"problem": 35, "solution": "55"},
    {"problem": 36, "solution": "872187"},
    {"problem": 37, "solution": "748317"},
    {"problem": 38, "solution": "932718654"},
    {"problem": 39, "solution": "840"},
    {"problem": 40, "solution": "210"},
    {"problem": 41, "solution": "7652413"},
    {"problem": 42, "solution": "162"},
    {"problem": 43, "solution": "16695334890"},
    {"problem": 44, "solution": "5482660"},
    {"problem": 45, "solution": "1533776805"},
    {"problem": 46, "solution": "5777"},
    {"problem": 47, "solution": "134043"},
    {"problem": 48, "solution": "9110846700"},
    {"problem": 49, "solution": "296962999629"},
    {"problem": 50, "solution": "997651"},
]


@pytest.mark.parametrize(
    ["problem", "solution"],
    [(item["problem"], item["solution"]) for item in SOLUTIONS],
    ids=[f'problem {item["problem"]}' for item in SOLUTIONS],
)
def test_problems(problem: int, solution: str) -> None:
    m = importlib.import_module(  # pylint: disable=invalid-name
        f"src.{problem:03d}.p{problem:03d}"
    )
    result = str(m.solve())
    assert result == solution
