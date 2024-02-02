class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort(reverse=True)
        lst = []
        # print(nums)
        for i in range(0,len(nums)-2,3):
            if nums[i] - nums[i+2] > k:
                return []
            lst.append(nums[i:i+3])
        return lst
        