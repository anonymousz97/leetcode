class Solution:
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])
        N = m * n

        num_to_index = [-1] * (N + 1)
        for i, num in enumerate(arr):
            num_to_index[num] = i

        row_painted = [0] * m
        col_painted = [0] * n

        row_pos = [0] * N
        col_pos = [0] * N
        for i in range(m):
            for j in range(n):
                num = mat[i][j]
                index_in_arr = num_to_index[num]
                row_pos[index_in_arr] = i
                col_pos[index_in_arr] = j

        for i, num in enumerate(arr):
            row_idx = row_pos[num_to_index[num]]
            col_idx = col_pos[num_to_index[num]]

            row_painted[row_idx] += 1
            col_painted[col_idx] += 1

            if row_painted[row_idx] == n or col_painted[col_idx] == m:
                return i

        return -1