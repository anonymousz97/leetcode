from heapq import heappop, heappush
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        cost = [[float('inf')] * n for _ in range(m)]
        heap = [(0, 0, 0)]  
        cost[0][0] = 0

        while heap:
            curr_cost, x, y = heappop(heap)

            if (x, y) == (m - 1, n - 1):
                return curr_cost

            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # Cost to move to (nx, ny)
                    new_cost = curr_cost + (1 if grid[x][y] != i + 1 else 0)
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heappush(heap, (new_cost, nx, ny))

        return -1
