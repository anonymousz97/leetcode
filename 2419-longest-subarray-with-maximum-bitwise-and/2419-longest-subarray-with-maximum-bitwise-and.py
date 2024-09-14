class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        max_len = 1
        cnt = 0
        flag = 0
        for i in nums:
            if i == max_value:
                if flag == 0:
                    flag = 1
                cnt += 1
            else:
                if cnt > max_len:
                    max_len = cnt
                if flag == 1:
                    flag = 0
                    cnt = 0
        if cnt > max_len:
            max_len = cnt
        return max_len
                    
        