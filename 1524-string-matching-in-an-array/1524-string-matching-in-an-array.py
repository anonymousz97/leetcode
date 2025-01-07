class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda s: len(s), reverse=True)
        lst = []
        res = []
        for i in words:
            flag = 0
            for j in lst:
                if i in j:
                    flag = 1
                    res.append(i)
                    break
            if not flag:
                lst.append(i)
        return res

        