class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        left, right = 0, sum(grid[0][1:])
        min_score = max(left, right)
        for i in range(1, len(grid[0])):
            left += grid[1][i-1]
            right -= grid[0][i]
            if min_score > max(left, right):
                min_score = max(left, right)
        return min_score

        