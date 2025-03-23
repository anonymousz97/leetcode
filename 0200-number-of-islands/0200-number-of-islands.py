class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        self.rows, self.cols = len(grid), len(grid[0])
        grid.insert(0, [0] * self.cols)
        grid.append([0] * self.cols)
        grid = [[0]+x+[0] for x in grid]
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt
                
        
    def dfs(self, grid, x, y):
        if grid[x][y] != '1':
            return
        grid[x][y] = "#"
        self.dfs(grid, x, y-1) # left
        self.dfs(grid, x-1, y) # up
        self.dfs(grid, x, y+1) # right
        self.dfs(grid, x+1, y) # bottom