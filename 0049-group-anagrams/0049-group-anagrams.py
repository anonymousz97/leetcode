class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f=defaultdict(list)
        for w in strs:
            wdsrted= ''.join(sorted(w))
            f[wdsrted].append(w)
        return list(f.values())