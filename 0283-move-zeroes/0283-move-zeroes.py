class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in nums:
            if j != 0:
                nums[i] = j
                i += 1
        for g in range(i, len(nums)):
            nums[g] = 0
        