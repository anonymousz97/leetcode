class Solution:

    def lowerBound(self, nums, r, l, v):
        ret = l + 1
        while r <= l:
            mid = int(r + (l - r) / 2)
            target = nums[mid]
            if target < v:
                r = mid + 1
            else:
                ret = mid
                l = mid - 1
        return ret

    def upperBound(self, nums, r, l, v):
        ret = l + 1
        while r <= l:
            mid = int(r + (l - r) / 2)
            target = nums[mid]
            if target <= v:
                r = mid + 1
            else:
                ret = mid
                l = mid - 1
        return ret


    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for idx in range(len(nums)):
            s = self.lowerBound(nums, idx+1, len(nums) - 1, lower - nums[idx])
            e = self.upperBound(nums, idx+1, len(nums) - 1, upper - nums[idx])

            if s <= len(nums) - 1:
                res += (e - s)
        return res



        