from collections import Counter
from typing import List


def single_number(nums: List[int]) -> int:
    return Counter(nums).most_common()[-1][0]
