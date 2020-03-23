import collections
from typing import List


def minIncrementForUnique(A: List[int]) -> int:
    A.sort()
    res = 0
    for i in range(len(A))[1:]:
        print(i)
        x = A[i]-A[i-1]
        if x <= 0:
            A[i] += abs(x) + 1
            res += abs(x) + 1
        else:
            continue
    return res

minIncrementForUnique([3,2,1,2,1,7])