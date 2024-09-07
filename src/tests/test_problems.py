import importlib
import json
import os.path
import pytest


answers_file = os.path.join(os.path.dirname(__file__), "../answers.json")
with open(answers_file, encoding="utf8") as f:
    ANSWERS = json.load(f)


@pytest.mark.parametrize(
    ["problem", "answer"],
    [(item["problem"], item["answer"]) for item in ANSWERS],
    ids=[f'problem {item["problem"]}' for item in ANSWERS],
)
def test_problems(problem: int, answer: str) -> None:
    m = importlib.import_module(  # pylint: disable=invalid-name
        f"src.P{problem:03d}.p{problem:03d}"
    )
    result = str(m.solve())
    assert result == answer
