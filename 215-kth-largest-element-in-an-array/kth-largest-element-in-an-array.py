import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(nums, k):
            pivot = nums[random.randint(0, len(nums)-1)]
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            leftlen = len(left)
            if k <= leftlen:
                return quickselect(left, k)
            if k > leftlen + len(mid):
                return quickselect(right, k-leftlen-len(mid))
            
            return pivot


        return quickselect(nums, k)