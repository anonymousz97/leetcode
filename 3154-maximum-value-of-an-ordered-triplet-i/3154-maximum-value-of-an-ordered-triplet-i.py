class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = -1
        for idx in range(1, len(nums)-1):
            left = nums[:idx]
            right = nums[idx+1:]
            if (max(left) - nums[idx]) * max(right) > max_value:
                max_value = (max(left) - nums[idx]) * max(right)
        if max_value == -1:
            return 0
        return max_value
        