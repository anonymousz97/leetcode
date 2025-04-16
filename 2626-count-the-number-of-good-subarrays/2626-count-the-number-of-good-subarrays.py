from collections import defaultdict

class Solution:
    def countGoodSubarrays(self, nums, k):
        freq_map = defaultdict(int)
        total_pairs = 0
        result = 0
        left = 0

        for right in range(len(nums)):
            num = nums[right]
            total_pairs += freq_map[num]
            freq_map[num] += 1
            while total_pairs >= k:
                result += len(nums) - right
                freq_map[nums[left]] -= 1
                total_pairs -= freq_map[nums[left]]
                left += 1
        return result
        
    def countGood(self, nums: List[int], k: int) -> int:
        return self.countGoodSubarrays(nums, k)
        