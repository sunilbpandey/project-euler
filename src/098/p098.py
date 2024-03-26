# pylint: disable=consider-using-enumerate
import os


def hash_word(word: str) -> str:
    return "".join(sorted(word))


def are_compatible(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    for i in range(1, len(word1)):
        if word1[i] == word1[i - 1] and word2[i] != word2[i - 1]:
            return False
        if word1[i] != word1[i - 1] and word2[i] == word2[i - 1]:
            return False
    return True


def add_to_group(groups: dict[str, list[str]], word: str) -> None:
    key = hash_word(word)
    if key not in groups:
        groups[key] = []
    groups[key].append(word)


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "0098_words.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    anagram_groups: dict[str, list[str]] = {}
    for word in content.split(","):
        add_to_group(anagram_groups, word.strip('"'))

    # Remove all groups with a single word, or with fewer than 3 letters
    anagram_groups = {
        k: v for k, v in anagram_groups.items() if len(k) > 3 and len(v) > 1
    }

    square_groups: dict[str, list[str]] = {}
    for num in range(32, 31623):
        add_to_group(square_groups, str(num * num))

    # Remove all groups with a single square
    square_groups = {k: v for k, v in square_groups.items() if len(v) > 1}

    for square_key, squares in sorted(square_groups.items(), reverse=True):
        for anagram_key, anagrams in anagram_groups.items():
            if not are_compatible(square_key, anagram_key):
                continue
            for i in range(len(squares)):
                mapping = dict(zip(squares[i], anagrams[0]))
                for j in range(len(squares)):
                    if j == i:
                        continue
                    translated = "".join([mapping[ch] for ch in squares[j]])
                    if translated == anagrams[1]:
                        return max(int(squares[i]), int(squares[j]))
    return 0
