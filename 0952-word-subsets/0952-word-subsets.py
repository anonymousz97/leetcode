import string

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # find substr diff char
        check = {i:0 for i in string.ascii_lowercase}
        for w in words2:
            tmp = {i:0 for i in string.ascii_lowercase}
            for c in w:
                tmp[c] += 1
            for item in tmp:
                if tmp[item] > check[item]:
                    check[item] = tmp[item]
        
        lst_verify = []
        for word in words1:
            tmp = {i:0 for i in string.ascii_lowercase}
            for c in word:
                tmp[c] += 1
            flag = 0
            for item in check:
                if (check[item] > tmp[item]) and check[item] != 0:
                    flag = 1
                    break
            if not flag:
                lst_verify.append(word)
        return lst_verify