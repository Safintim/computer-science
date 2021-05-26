from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """

    shift = arr.count(0)
    l = len(arr)
    for i in range(l - 1, -1, -1):
        if i + shift < l:
            arr[i + shift] = arr[i]
        if arr[i] == 0:
            shift -= 1
            if i + shift < l:
                arr[i + shift] = 0
