from functools import reduce
from operator import xor
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        cur_s = [0 for x in range(len(nums))]
        s = 0
        while sum(cur_s) != len(nums):
            for i in range(len(nums)-1,-1,-1):
                if cur_s[i] == 0:
                    cur_s[i] = 1
                    for j in range(i+1, len(nums)):
                        cur_s[j] = 0
                    break
            # add new xor
            tmp = []
            for idx in range(len(cur_s)):
                if cur_s[idx] == 1:
                    tmp.append(nums[idx])

            s += reduce(xor, tmp)
        return s

        