from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = defaultdict(int)
        for idx, i in enumerate(nums):
            if counts[target - i] != 0:
                return [counts[target - i] - 1, idx]
            counts[i] = idx + 1
                
        