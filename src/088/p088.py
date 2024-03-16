import math


def solve() -> int:
    min_prod_sum: dict[int, int] = {}
    for length in range(2, 15):
        nums = [2] * length
        while True:
            product = math.prod(nums)
            if product > 24000:
                # find the first value smaller than the previous one
                # if no such index is found, we are done for this length
                try:
                    idx = next(i for i in range(1, len(nums)) if nums[i] < nums[i - 1])
                except StopIteration:
                    break

                # increment this number, and reset all the numbers before it
                nums[idx] += 1
                for i in range(0, idx):
                    nums[i] = nums[idx]
                continue

            k = product - sum(nums) + length
            if 2 <= k <= 12000:
                min_prod_sum[k] = (
                    product if k not in min_prod_sum else min(min_prod_sum[k], product)
                )
            nums[0] += 1
    return sum(set(min_prod_sum.values()))
