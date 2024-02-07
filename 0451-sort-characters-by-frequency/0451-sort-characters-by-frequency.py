class Solution:
    def frequencySort(self, s: str) -> str:
        dup = {}
        for i in s:
            if i not in dup.keys():
                dup[i] = 1
            else:
                dup[i] += 1
        sortedDict = sorted(dup.items(), key=lambda x:x[1], reverse=True)
        # print(sortedDict, dup)
        r = ""
        for i in sortedDict:
            r += i[0] * i[1]
        return r