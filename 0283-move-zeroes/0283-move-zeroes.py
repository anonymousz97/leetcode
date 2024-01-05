class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        j = i - 1
        while True:
            if j < 0:
                break
            if nums[j] == 0:
                for g in range(j, i):
                    nums[g], nums[g+1] = nums[g+1], nums[g]
                i -= 1
            j -= 1
        print(nums)
        