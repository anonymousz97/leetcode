class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        idx_1 = idx_2 = 0
        res = []
        while True:
            if idx_1 < len(nums1) and idx_2 < len(nums2):
                if nums1[idx_1][0] == nums2[idx_2][0]:
                    res.append([nums1[idx_1][0], nums1[idx_1][1] + nums2[idx_2][1]])
                    idx_1 += 1
                    idx_2 += 1
                elif nums1[idx_1][0] < nums2[idx_2][0]:
                    res.append(nums1[idx_1])
                    idx_1 += 1
                else:
                    res.append(nums2[idx_2])
                    idx_2 += 1
            elif idx_1 < len(nums1):
                res.append(nums1[idx_1])
                idx_1 += 1
            elif idx_2 < len(nums2):
                res.append(nums2[idx_2])
                idx_2 += 1
            else:
                break
        return res

        