from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mapping_pos = {i:j for j, i in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        max_length = 0
        for i in range(len(arr)):
            for j in range(i):
                tmp = arr[i] - arr[j]
                if tmp in mapping_pos and mapping_pos[tmp] < j:
                    dp[j, i] = dp[mapping_pos[tmp], j] + 1
                    max_length = max(dp[j, i], max_length)
        return max_length if max_length >=3 else 0


        