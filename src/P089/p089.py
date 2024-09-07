import os


ROMAN_TO_DECIMAL = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


DECIMAL_TO_ROMAN = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


def roman_to_decimal(roman: str) -> int:
    number = 0
    prev = ""
    # pylint: disable=invalid-name
    for ch in roman:
        if prev != "" and ROMAN_TO_DECIMAL[prev] < ROMAN_TO_DECIMAL[ch]:
            number -= 2 * ROMAN_TO_DECIMAL[prev]
        number += ROMAN_TO_DECIMAL[ch]
        prev = ch
    # pylint: enable=invalid-name
    return number


def decimal_to_roman(decimal: int) -> str:
    roman = ""
    while decimal > 0:
        num = next(
            n for n in sorted(DECIMAL_TO_ROMAN.keys(), reverse=True) if decimal >= n
        )
        roman += DECIMAL_TO_ROMAN[num]
        decimal -= num
    return roman


def solve1() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "0089_roman.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    chars_saved = 0
    for line in content.splitlines():
        roman = decimal_to_roman(roman_to_decimal(line))
        chars_saved += len(line) - len(roman)
    return chars_saved


REPLACEMENTS = [
    ("DCCCC", "CM"),
    ("CCCC", "CD"),
    ("LXXXX", "XC"),
    ("XXXX", "XL"),
    ("VIIII", "IX"),
    ("IIII", "IV"),
]


def solve() -> int:
    input_path = os.path.join(os.path.dirname(__file__), "0089_roman.txt")
    with open(input_path, encoding="utf8") as file:
        content = file.read()

    chars_saved = 0
    for line in content.splitlines():
        optimal = line
        for old, new in REPLACEMENTS:
            optimal = optimal.replace(old, new)
        chars_saved += len(line) - len(optimal)
    return chars_saved
