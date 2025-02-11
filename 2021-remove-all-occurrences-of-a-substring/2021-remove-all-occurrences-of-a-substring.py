class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            tmp = s.replace(part, "", 1)
            if len(tmp) == len(s):
                return tmp
            s = tmp
        