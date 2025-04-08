class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        print(dct)
        cnt = 0
        while True:
            flag = 0
            for i in dct.keys():
                if dct[i] > 1:
                    flag = 1
                    if len(nums) < 3:
                        cnt += 1
                        dct = {}
                        return cnt
                    # do operation
                    dct[nums[0]] -= 1
                    dct[nums[1]] -= 1
                    dct[nums[2]] -= 1
                    nums = nums[3:]
                    cnt += 1
            if not flag:
                return cnt
        