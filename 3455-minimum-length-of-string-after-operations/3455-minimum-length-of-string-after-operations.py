class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        res = {}
        for i in s:
            if ord(i) - ord('a') not in res.keys():
                res[ord(i) - ord('a')] = 1
            else:
                res[ord(i) - ord('a')] += 1
        cnt = 0
        for i in res.keys():
            cnt += (res[i] - 1)//2
        return len(s) - 2 * cnt