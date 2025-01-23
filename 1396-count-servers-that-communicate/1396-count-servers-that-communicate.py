class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cnt = 0
        grid_t = list(zip(*grid))
        lst_r = []
        for idx, i in enumerate(grid):
            if sum(i) > 1:
                cnt += sum(i)
                lst_r.append(idx)

        lst_c = []
        for idx, i in enumerate(grid_t):
            if sum(i) > 1:
                cnt += sum(i)
                lst_c.append(idx)

        for i in lst_r:
            for j in lst_c:
                if grid[i][j] == 1:
                    cnt -= 1
        return cnt
        