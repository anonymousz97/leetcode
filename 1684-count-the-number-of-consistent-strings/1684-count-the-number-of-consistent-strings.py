class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        value = [False] * 26
        cnt = 0
        for i in allowed:
            value[ord(i) - ord('a')] = True
        for word in words:
            flag = 0
            for character in word:
                if not value[ord(character)- ord('a')]:
                    flag = 1
                    break
            if flag:
                continue
            cnt += 1
        return cnt