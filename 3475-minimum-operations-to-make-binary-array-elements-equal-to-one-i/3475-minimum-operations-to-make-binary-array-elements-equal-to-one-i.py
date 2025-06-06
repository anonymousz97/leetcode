class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flips = 0
        for i in range(n - 2): 
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]  
                nums[i + 2] = 1 - nums[i + 2] 
                flips += 1  
        return flips if nums[-2:] == [1, 1] or n < 3 else -1