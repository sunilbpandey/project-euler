import itertools


def solve1() -> int:
    total = 0
    for number in itertools.permutations(range(10)):
        if number[0] == 0:
            continue
        if number[3] % 2 != 0:
            continue
        if number[5] % 5 != 0:
            continue
        if (number[2] + number[3] + number[4]) % 3 != 0:
            continue
        if (number[4] * 100 + number[5] * 10 + number[6]) % 7 != 0:
            continue
        if (number[5] * 100 + number[6] * 10 + number[7]) % 11 != 0:
            continue
        if (number[6] * 100 + number[7] * 10 + number[8]) % 13 != 0:
            continue
        if (number[7] * 100 + number[8] * 10 + number[9]) % 17 != 0:
            continue
        total += int("".join(str(d) for d in number))
    return total


def solve() -> int:
    total = 0

    # the next divisor to check, based on the number of digits in number
    # e.g., if the current number is 4 digits long, before adding the next digit,
    # we should check if the number formed by taking the last two digits and
    # the new digit is divisible by the divisor at index 4 in the list, i.e. 3.
    divisors = [1, 1, 1, 2, 3, 5, 7, 11, 13, 17]

    # instead of recursion, use a queue to store the numbers we are building
    # intialize the queue with the first digit; first digit cannot be 0
    queue = list(range(1, 10))
    while queue:
        number = queue.pop()
        sub_number = (number % 100) * 10
        num_string = str(number)
        for digit in range(10):
            if (sub_number + digit) % divisors[len(num_string)] != 0:
                continue
            if str(digit) in num_string:
                continue
            new_number = number * 10 + digit
            if len(num_string) == 9:
                total += new_number
            else:
                queue.append(new_number)
    return total
