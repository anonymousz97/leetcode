class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = abs(nums[0])
        c_sum = (nums[0], nums[0])
        max_value = abs(nums[0])
        for idx, i in enumerate(nums[1:]):
            dp[idx] = max(abs(c_sum[0]+i), abs(i), abs(c_sum[1]+i))
            if dp[idx] > max_value: max_value = dp[idx]
            c_sum = (max(c_sum[0]+i, i, c_sum[1]+i), min(c_sum[0]+i, i, c_sum[1]+i))
            # print(i, max_value, c_sum)
        return max_value

        