class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx, i in enumerate(s):
            if s.count(i) == 1:
                return idx
        return -1
        