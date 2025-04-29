from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_value = max(nums)
        cnt = 0
        count_max = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == max_value:
                count_max += 1
            while count_max >= k:
                if nums[left] == max_value:
                    count_max -= 1
                left += 1
            cnt += left
        return cnt