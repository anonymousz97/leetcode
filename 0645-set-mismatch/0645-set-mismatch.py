class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dups = 0
        a = [x for x in range(1,len(nums)+1,1)]
        for i in nums:
            try:
                a.remove(i)
            except:
                dups = i
        return [dups, a[0]]
        