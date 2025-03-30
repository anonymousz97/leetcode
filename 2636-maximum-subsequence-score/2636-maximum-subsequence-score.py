import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        tmp = [(a, b) for a, b in zip(nums1, nums2)]
        tmp.sort(key=lambda x: x[1], reverse=True)
        max_v = -1
        lst = []
        sum_first_part = 0
        heapq.heapify(lst)
        for j in tmp:
            heapq.heappush(lst, j)
            sum_first_part += j[0]
            if len(lst) > k:
                t = heapq.heappop(lst)
                sum_first_part -= t[0]
            if len(lst) == k:
                max_v = max(max_v, sum_first_part * j[1])
        return max_v



        