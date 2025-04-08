class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        n = len(nums)
        cnt = 0
        l = 0
        max_num = max(nums)
        freq = 0

        for r in range(n):
            if nums[r] == max_num:
                freq += 1

            while freq >= k:
                cnt += n - r
                if nums[l] == max_num:
                    freq -= 1
                l += 1

        return cnt