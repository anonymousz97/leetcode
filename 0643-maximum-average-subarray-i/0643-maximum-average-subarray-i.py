class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        init = sum(nums[:k])
        maxAvg = init
        for i in range(k,len(nums)):
            tmp = init + nums[i] - nums[i-k]
            init = tmp
            if maxAvg < tmp:
                maxAvg = tmp
            # print(tmp)
        return maxAvg/k
        