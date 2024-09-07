import math
import os.path


LETTER_SCORES = {chr(ord("A") + i): i + 1 for i in range(26)}


def get_word_score(word: str) -> int:
    return sum(LETTER_SCORES[char] for char in word)


def is_triangle_number(number: int) -> bool:
    return math.sqrt(8 * number + 1) % 1 == 0


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "p042_words.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()
    words = sorted(word.strip('"') for word in content.split(","))
    return sum(1 for w in words if is_triangle_number(get_word_score(w)))
