def solve() -> int:
    chain_lengths = [0] * 1000000
    chain_lengths[1] = 1

    max_chain_length = 0
    max_chain_length_start = 0

    for start in range(500000, 1000000):
        chain_length = 0
        num = start
        while True:
            if num % 2 == 0:
                num = num // 2
                if num < start:
                    chain_lengths[start] = chain_length + chain_lengths[num]
                    break
            else:
                num = 3 * num + 1
            chain_length += 1

        if chain_lengths[start] > max_chain_length:
            max_chain_length = chain_lengths[start]
            max_chain_length_start = start
    return max_chain_length_start
