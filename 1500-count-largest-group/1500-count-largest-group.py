class Solution:
    def countLargestGroup(self, n: int) -> int:
        dct = {}
        max_v = 0
        for i in range(1, n+1):
            tmp = sum([int(x) for x in str(i)])
            if tmp not in dct:
                dct[tmp] = 1
            else:
                dct[tmp] += 1
            if dct[tmp] > max_v:
                max_v = dct[tmp]
        cnt = 0
        for i in dct:
            if dct[i] == max_v:
                cnt += 1
        return cnt
        