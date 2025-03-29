from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # 1. Đưa tất cả quả cam thối vào queue + đếm số quả cam tươi
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # thêm cả phút hiện tại
                elif grid[r][c] == 1:
                    fresh += 1

        # 2. BFS từ các cam thối
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        time = 0

        while q:
            r, c, t = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # làm cam này thối
                    fresh -= 1
                    q.append((nr, nc, t + 1))
                    time = max(time, t + 1)

        return time if fresh == 0 else -1