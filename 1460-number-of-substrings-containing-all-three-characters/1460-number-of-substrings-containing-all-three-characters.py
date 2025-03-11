from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dct_pos = defaultdict(list)
        for idx in range(len(s)):
            dct_pos[s[idx]].append(idx)

        if len(dct_pos) != 3:
            return 0

        cnt = 0
        while True:
            min_p = []
            min_pos = ''
            for i in dct_pos:
                if dct_pos[i] == []:
                    return cnt
                min_p.append(dct_pos[i][0])
                if min(min_p) == dct_pos[i][0]:
                    min_pos = i
            cnt += len(s) - max(min_p)
            dct_pos[min_pos] = dct_pos[min_pos][1:]




            

        