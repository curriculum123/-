from typing import List


def Solution(arr: List[int], k: int) -> int:
    arr.sort()
    return arr[:k]

print(Solution([3,1,2], 2))
