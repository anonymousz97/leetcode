class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        if k == min(nums):
            return len(list(set(nums))) - 1
        return len(list(set(nums)))
        