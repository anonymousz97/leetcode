class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        dif = -1
        val = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= val:
                val = nums[i]
            else:
                dif = max(dif, val - nums[i])
        return dif

        