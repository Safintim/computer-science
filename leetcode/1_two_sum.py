from typing import List


def two_sum(self, nums: List[int], target: int) -> List[int]:
    cache = {}

    for i, num in enumerate(nums):
        dif = target - num
        if dif in cache:
            return [cache[dif], i]
        cache[num] = i
    return []
