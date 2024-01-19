class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        a = {}
        for i in word1:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        
        w1 = list(a.values())
        b = {}
        for i in word2:
            if i not in b.keys():
                b[i] = 1
            else:
                b[i] += 1
        
        if len([x for x in b.keys() if x not in a.keys()]) > 0:
            return False
        for i in a.keys():
            try:
                for j in b.keys():
                    if a[i] == b[j]:
                        del b[j]
            except:
                continue
        if len(list(b.keys())) == 0:
            return True
        return False
        