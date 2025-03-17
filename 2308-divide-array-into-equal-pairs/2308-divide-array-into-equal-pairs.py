from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = defaultdict(int)
        for i in nums:
            res[i] += 1
        for i,j in res.items():
            if j % 2 != 0:
                return False
        return True

        