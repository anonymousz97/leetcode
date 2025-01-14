class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        tmpA = [1] * len(A)
        tmpB = [1] * len(A)
        res = []
        cnt = 0
        for i in range(len(A)):
            tmpA[A[i]-1] = 0
            tmpB[B[i]-1] = 0
            if B[i] == A[i]:
                cnt += 1
                res.append(cnt)
                continue
            if tmpA[B[i]-1] == 0:
                cnt += 1
            if tmpB[A[i]-1] == 0:
                cnt += 1
            res.append(cnt)
        return res
        