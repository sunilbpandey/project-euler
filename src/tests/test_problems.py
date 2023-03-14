import importlib
import pytest

SOLUTIONS = [
    {"problem": 1, "solution": "233168"},
    {"problem": 2, "solution": "4613732"},
    {"problem": 3, "solution": "6857"},
    {"problem": 4, "solution": "906609"},
    {"problem": 5, "solution": "232792560"},
    {"problem": 6, "solution": "25164150"},
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
