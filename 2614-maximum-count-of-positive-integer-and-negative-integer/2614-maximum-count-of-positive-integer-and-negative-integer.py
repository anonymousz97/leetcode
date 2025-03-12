class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0 or nums[i] > 0:
                return max(i, len(nums)-nums.count(0)-i)
        return len(nums)   
        