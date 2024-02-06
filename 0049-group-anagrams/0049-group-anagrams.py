class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st = []
        res = []
        for i in strs:
            tmp = [0] * 26
            for j in i:
                tmp[ord(j)-ord('a')] += 1
            if tmp not in st:
                st.append(tmp)
                res.append([i])
            else:
                idx = st.index(tmp)
                res[idx].append(i)
        return res