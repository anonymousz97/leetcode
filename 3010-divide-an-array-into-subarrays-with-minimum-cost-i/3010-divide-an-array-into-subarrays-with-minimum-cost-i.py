class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        t = nums[0]
        nums = nums[1:]
        nums.sort()
        return t + nums[0] + nums[1]
        