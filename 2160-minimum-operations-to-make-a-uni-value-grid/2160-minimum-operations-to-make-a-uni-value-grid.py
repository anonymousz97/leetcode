class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        lst = sorted([i for s in grid for i in s])
        mid = len(lst) // 2
        median = lst[mid]
        tc = 0
        for v in lst:
            if abs(v - median) % x != 0:
                return -1
            tc += abs(v - median) // x
        return tc