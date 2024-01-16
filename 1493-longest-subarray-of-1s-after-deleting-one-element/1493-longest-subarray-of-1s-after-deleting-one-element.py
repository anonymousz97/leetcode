class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s = 0
        e = 0
        c = 1
        while e < len(nums):
            c -= 1-nums[e]
            e += 1
            if c < 0:
                c += 1 - nums[s]
                s += 1
        return e-s-1
                
        