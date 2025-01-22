class Solution:
    def highestPeak(self, isWater):
        m = len(isWater)
        n = len(isWater[0])

        # Initialize result matrix with the same dimensions as input
        matrix = [[float('inf')] * n for _ in range(m)]

        # Initialize the matrix
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    matrix[i][j] = 0  # Water cells have height 0

        # Forward pass from (0, 0) based on upper and left cells
        directions = [(-1, 0), (0, -1)]  # LEFT and DOWN directions
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        matrix[i][j] = min(matrix[i][j], matrix[ni][nj] + 1)

        # Backward pass from (m-1, n-1) based on down and right cells
        directions = [(1, 0), (0, 1)]  # RIGHT and UPPER directions
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        matrix[i][j] = min(matrix[i][j], matrix[ni][nj] + 1)

        return matrix
