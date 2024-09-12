class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for i in words:
            if sum([i.count(j) for j in allowed]) == len(i):
                cnt += 1
        return cnt