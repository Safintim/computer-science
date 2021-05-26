from typing import List


def two_sum(self, nums: List[int], target: int) -> List[int]:
    cache = {}

    for i, num in enumerate(nums):
        dif = target - num
        if dif in cache:
            return [cache[dif], i]
        cache[num] = i
    return []


class Line:
    def __init__(self, w) -> None:
        self.__w = w
    
    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, v):
        self.__w = v

    


a=Line(10)
print(a.w)
a.w = 1
print(a.w)
print(type(a.w))