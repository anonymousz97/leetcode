class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dct_map = {0:0}
        max_l = 0
        n = 0
        for idx, i in enumerate(nums):
            if i == 0:
                n += 1
            else:
                n -= 1
            if n not in dct_map:
                dct_map[n] = idx+1
            else:
                if max_l < (idx+1) - dct_map[n]:
                    max_l = (idx+1) - dct_map[n]
        return max_l
        