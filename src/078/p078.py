import itertools


def solve() -> int:
    pentagonal = [1, 2]
    for k in range(2, 200):
        pentagonal.append(pentagonal[-2] + 3 * k - 2)
        pentagonal.append(pentagonal[-2] + 3 * k - 1)

    partitions = [1, 1]
    answer = 0
    for num in itertools.count(2):
        partitions.append(0)
        sign = 1
        for k in range(1, num):
            term1 = pentagonal[2 * k - 2]
            subtotal = partitions[num - term1] if term1 <= num else 0

            term2 = pentagonal[2 * k - 1]
            subtotal += partitions[num - term2] if term2 <= num else 0

            partitions[num] += sign * subtotal
            if term1 > num or term2 > num:
                break
            sign = -1 if sign == 1 else 1
        partitions[num] %= 1000000
        if partitions[num] == 0:
            answer = num
            break
    return answer
