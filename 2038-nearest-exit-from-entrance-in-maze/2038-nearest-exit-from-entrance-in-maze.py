class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze) , len(maze[0])
        q = deque()
        direction = [(-1,0), (0,-1), (1,0), (0,1)]
        visited = set()
        q.append((entrance[0], entrance[1], 0))
        visited.add((entrance[0], entrance[1]))
        while q:
            row, col, step = q.popleft()
            for (r_m, c_m) in direction:
                n_r, n_c = row+r_m, col+c_m
                if 0 <= n_r < m and 0 <= n_c < n and maze[n_r][n_c] == '.' and (n_r, n_c) not in visited:
                    if n_r == 0 or n_r == m - 1 or n_c == 0 or n_c == n - 1:
                        return step + 1
                    q.append((n_r, n_c, step+1))
                    visited.add((n_r, n_c))
        return -1
            
