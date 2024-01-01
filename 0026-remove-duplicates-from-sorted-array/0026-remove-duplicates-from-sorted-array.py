class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = list(set(nums))
        t.sort()
        t = t[::-1]
        for i in t:
            nums.insert(0,i)
        return len(t) 
        