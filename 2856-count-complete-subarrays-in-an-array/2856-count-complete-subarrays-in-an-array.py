class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_num = len(list(set(nums)))
        dct = {}
        cnt = 0
        l = 0
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
            if len(dct) != distinct_num:
                continue
            while True:
                if dct[nums[l]] > 1:
                    dct[nums[l]] -= 1
                    l += 1
                else:
                    cnt += l + 1
                    break
        return cnt

        