class Solution:
    def rob(self, nums: List[int]) -> int:
        use = [0] * len(nums)
        max_s = [0] * len(nums)
        max_s[0] = nums[0]
        use[0] = 1
        for i in range(1, len(use), 1):
            if use[i-1] == 1:
                if max_s[i-1] > max_s[i-2] + nums[i]:
                    use[i] = 1
                    max_s[i] = max_s[i-1]
                else:
                    use[i] = 1
                    use[i-1] = 0
                    max_s[i] = max_s[i-2] + nums[i]
            else:
                max_s[i] = max_s[i-1] + nums[i]
                use[i] = 1
        return max(max_s)