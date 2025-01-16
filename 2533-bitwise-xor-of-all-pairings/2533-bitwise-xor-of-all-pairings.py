class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        elif len(nums1) % 2 == 1 and len(nums2) % 2 == 1:
            tmp = nums1 + nums2
            s = tmp[0]
            for i in tmp[1:]:
                s ^= i
            return s
        else:
            if len(nums1) % 2 == 0:
                s = nums1[0]
                for i in nums1[1:]:
                    s ^= i
                return s
            else:
                s = nums2[0]
                for i in nums2[1:]:
                    s ^= i
                return s
        