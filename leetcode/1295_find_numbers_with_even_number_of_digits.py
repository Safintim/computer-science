
from typing import List


def findNumbers(nums: List[int]) -> int:
    return len([n for n in nums if len(str(n)) % 2 == 0])
