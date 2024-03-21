def solve() -> int:
    limit = 1_000_000
    sum_of_divisors = [1] * (limit + 1)
    for i in range(2, limit + 1):
        for j in range(i * 2, len(sum_of_divisors), i):
            sum_of_divisors[j] += i

    longest_chain = 0
    longest_chain_start = limit
    for start in range(2, limit):
        tortoise, hare = start, start
        chain_length = 0
        while True:
            # if the tortoise is less than the start
            # then start is not the smallest number in the chain
            if tortoise < start:
                break

            if sum_of_divisors[hare] > limit:
                break

            tortoise = sum_of_divisors[tortoise]
            hare = sum_of_divisors[sum_of_divisors[hare]]
            if tortoise > limit or hare > limit:
                break

            chain_length += 1
            if tortoise == hare:
                if tortoise == start and chain_length > longest_chain:
                    longest_chain = chain_length
                    longest_chain_start = start
                break
    return longest_chain_start
