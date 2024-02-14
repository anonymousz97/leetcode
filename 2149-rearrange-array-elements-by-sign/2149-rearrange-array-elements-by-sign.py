class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst_pos = []
        lst_neg = []
        for i in nums:
            if i > 0:
                lst_pos.append(i)
            else:
                lst_neg.append(i)
        res = []
        while len(res) != len(nums):
            res.append(lst_pos.pop(0))
            res.append(lst_neg.pop(0))
        return res
        