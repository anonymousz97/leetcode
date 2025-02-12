class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dct_sum_num = {}
        max_value = -1
        for i in nums:
            tmp = 0
            for j in str(i):
                tmp += int(j)
            if tmp in dct_sum_num.keys():
                if i + dct_sum_num[tmp] > max_value:
                    max_value = i + dct_sum_num[tmp]
                if i > dct_sum_num[tmp]:
                    dct_sum_num[tmp] = i
            else:
                dct_sum_num[tmp] = i
        return max_value

        