from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_count = count = 0
    for n in nums:
        if n == 0:
            max_count = max(max_count, count)
            count = 0
        else:
            count += 1
    return max(max_count, count)
