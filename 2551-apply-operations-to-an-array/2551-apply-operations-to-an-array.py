class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                nums[idx] *= 2
                nums[idx+1] = 0
            if nums[idx] != 0:
                res.append(nums[idx])
        if nums[len(nums)-1] != 0:
            res.append(nums[len(nums)-1])
        return res + [0] * (len(nums) - len(res))
        