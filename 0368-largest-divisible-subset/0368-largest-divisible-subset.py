class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[i] for i in range(len(nums))]
        dp[0] = [0]
        for i in range(1, len(nums)):
            max_idx = [] 
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if len(max_idx) < len(dp[j]):
                        max_idx = dp[j]
            dp[i] = max_idx + [i]
        return [nums[i] for i in max(dp, key=len)]

        