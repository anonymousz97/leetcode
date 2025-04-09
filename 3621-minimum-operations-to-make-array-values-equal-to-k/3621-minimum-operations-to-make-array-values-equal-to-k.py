class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = min(nums)
        t = len(list(set(nums)))
        if k > m:
            return -1
        if k == m:
            return t - 1
        return t
        