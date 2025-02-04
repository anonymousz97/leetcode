class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        pivot = nums[0]
        max_s = nums[0]
        c_s = nums[0]
        for i in nums[1:]:
            if i <= pivot:
                if c_s > max_s:
                    max_s = c_s
                    c_s = i
                else:
                    c_s = i
            else:
                c_s += i
            pivot = i
        if c_s > max_s:
            max_s = c_s
        return max_s