from typing import cast
import importlib
import unittest

solutions = [
    {"problem": 1, "solution": "233168"},
]


class TestProjectEuler(unittest.TestCase):
    def __test(self, problem: int, solution: str) -> None:
        try:
            m = importlib.import_module(  # pylint: disable=invalid-name
                f"src.{problem:03d}.p{problem:03d}"
            )
            result = str(m.solve())
            self.assertEqual(result, solution)
        except ModuleNotFoundError:
            pass

    def test(self) -> None:
        for solution in solutions:
            with self.subTest(
                problem=solution["problem"], solution=solution["solution"]
            ):
                self.__test(
                    cast(int, solution["problem"]), cast(str, solution["solution"])
                )
        with self.subTest():
            self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
