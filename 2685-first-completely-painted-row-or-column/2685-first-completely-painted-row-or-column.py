class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        tmp = []
        dct_score = {}
        map_pos = {}
        m, n = len(mat), len(mat[0])
        for j in range(n):
            dct_score[f'col{j}'] = 0
        for idx, i in enumerate(mat):
            tmp += i
            dct_score[f"row{idx}"] = sum(i)
            for j in range(n):
                dct_score[f'col{j}'] += i[j]
                map_pos[i[j]] = (idx, j)

        for dix, i in enumerate(arr):
            idx_r, idx_c = map_pos[i]
            dct_score[f'row{idx_r}'] -= i
            dct_score[f'col{idx_c}'] -= i
            if dct_score[f'row{idx_r}'] == 0 or dct_score[f'col{idx_c}'] == 0:
                return dix



        