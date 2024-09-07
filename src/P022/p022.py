import os.path


def get_name_value(name: str) -> int:
    return sum(ord(char) - ord("A") + 1 for char in name)


def get_name_score(name: str, index: int) -> int:
    return get_name_value(name) * (index + 1)


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "p022_names.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()
    names = sorted(name.strip('"') for name in content.split(","))
    return sum(get_name_score(name, index) for index, name in enumerate(names))
