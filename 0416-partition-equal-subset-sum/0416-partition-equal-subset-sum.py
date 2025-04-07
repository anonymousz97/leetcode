class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        sum_find = sum(nums) // 2
        dp = [False for _ in range(sum(nums))]
        dp[0] = True
        for i in nums:
            for j in range(sum_find, i-1, -1):
                dp[j] = dp[j] or dp[j-i]
        if dp[sum_find]:
            return True
        print(dp)
        return False
        