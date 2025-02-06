def n(x):
    a = 1
    for i in range(1,x+1, 1):
        a *= i
    return a

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        lst = {}
        cnt = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums), 1):
                if nums[i] * nums[j] not in lst.keys():
                    lst[nums[i] * nums[j]] = 1
                else:
                    lst[nums[i] * nums[j]] += 1
        print(lst)
        for i, j in lst.items():
            if j > 1:
                cnt += 4 * j * (j-1)
        return int(cnt)


        