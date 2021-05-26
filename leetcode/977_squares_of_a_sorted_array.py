from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    return list(sorted(n ** 2 for n in nums))
