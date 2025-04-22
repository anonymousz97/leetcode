class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = 0
        dct_v = {}
        for i in answers:
            if i not in dct_v:
                dct_v[i] = 1
            else:
                dct_v[i] += 1
        for i in dct_v:
            tmp = dct_v[i] - (dct_v[i] // (i+1)) * (i+1)
            if tmp == 0:
                continue
            cnt += (i+1) - tmp
        return cnt+len(answers)

        