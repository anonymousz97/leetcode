class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            tmp = [x[i] for x in grid]
            cnt += grid.count(tmp)
        return cnt
        