names = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def get_number_name(num: int) -> str:
    if num in names:
        return names[num]

    if num < 100:
        return names[(num // 10) * 10] + names[num % 10]

    if num < 1000:
        name = f"{names[num // 100]}hundred"
        if num % 100 != 0:
            name += f"and{get_number_name(num % 100)}"
        return name

    return "onethousand"


def solve() -> int:
    return sum(len(get_number_name(num)) for num in range(1, 1001))
