"""
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例 1：
输入：[[2]]
输出：10

示例 2：
输入：[[1,2],[3,4]]
输出：34

示例 3：
输入：[[1,0],[0,2]]
输出：16

示例 4：
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32

示例 5：
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
"""
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        block = 0
        cover = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    block += grid[i][j]
                    cover += grid[i][j] - 1
                if i > 0:
                    cover += min(grid[i - 1][j], grid[i][j])
                if j > 0:
                    cover += min(grid[i][j - 1], grid[i][j])
        return block * 6 - cover * 2


s = Solution()
print(s.surfaceArea([[1,2],[3,4]]))