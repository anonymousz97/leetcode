class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        k_s1 = {}
        k_s2 = {}
        for i in s1.split(" "):
            if i not in k_s1.keys():
                k_s1[i] = 1
            else:
                k_s1[i] += 1
        # k_s1 = {k:v for k,v in k_s1.items() if v == 1}
        for i in s2.split(" "):
            if i not in k_s2.keys():
                k_s2[i] = 1
            else:
                k_s2[i] += 1
        # k_s2 = {k:v for k,v in k_s2.items() if v == 1}
        print(k_s1, k_s2)
        return [x for x in k_s1.keys() if x not in k_s2.keys() and k_s1[x] == 1] + [x for x in k_s2.keys() if x not in k_s1.keys() and k_s2[x] == 1]