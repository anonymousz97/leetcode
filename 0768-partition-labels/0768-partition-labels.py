class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dct_pos = {}
        res = []
        start = 0
        end = 0
        for idx, i in enumerate(s):
            dct_pos[i] = idx
        for idx, i in enumerate(s):
            if end < dct_pos[i]:
                end = dct_pos[i]
            if idx == end:
                res.append(end-start+1)
                start = idx + 1
                end = start
        return res


        