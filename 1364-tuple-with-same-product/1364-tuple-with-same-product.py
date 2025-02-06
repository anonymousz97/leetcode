from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        lst = defaultdict(int)
        cnt = 0

        # Count product frequencies
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                lst[product] += 1

        # Calculate result using direct combination formula
        for freq in lst.values():
            if freq > 1:
                cnt += 8 * (freq * (freq - 1)) // 2  # Efficient combination

        return cnt
