class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair = 0
        tmp = {}
        for i in nums:
            if i not in tmp.keys():
                tmp[i] = 1
            else:
                tmp[i] += 1
        if k//2 in tmp.keys() and k % 2 == 0:
            tmp[k//2] = tmp[k//2] // 2
        print(tmp)
        check = 0
        for i in list(set(nums)):
            if (k-i) in tmp.keys():
                    pair += min(tmp[i], tmp[k-i])
                    try:
                        del tmp[i]
                        del tmp[k-i]
                    except:
                        continue
        return pair
            
                
        