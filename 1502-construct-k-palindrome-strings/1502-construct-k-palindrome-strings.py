class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        if k == len(s):
            return True
        tmp = [0] * 26
        for i in s:
            tmp[ord(i)-ord('a')] += 1
        cnt = 0
        for i in tmp:
            if i % 2 == 1:
                cnt += 1
        if cnt > k:
            return False
        return True
        