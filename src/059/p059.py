import os
import itertools


def is_common_english_char(char: int) -> bool:
    return 32 <= char <= 122 and char not in [96]


def decipher(ciphertext: list[int], key: list[int]) -> list[int]:
    text: list[int] = []
    for index, char in enumerate(ciphertext):
        decrypted = char ^ key[index % 3]
        if not is_common_english_char(decrypted):
            return []
        text.append(decrypted)
    return text


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "p059_cipher.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()
    ciphertext = [int(c) for c in content.split(",")]

    text: list[int] = []

    # pylint: disable=invalid-name
    for a, b, c in itertools.permutations(range(ord("a"), ord("z") + 1), 3):
        key = [a, b, c]
        text = decipher(ciphertext, key)
        if text:
            break
    # pylint: enable=invalid-name
    return sum(text)
