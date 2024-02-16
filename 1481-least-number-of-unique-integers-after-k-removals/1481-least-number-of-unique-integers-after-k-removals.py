class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dct = {}
        len_dct = 0
        for i in arr:
            if i not in dct.keys():
                dct[i] = 1
                len_dct += 1
            else:
                dct[i] += 1
        sorted_dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
        keys = list(sorted_dct.keys())
        for idx, i in enumerate(keys):
            if k > 0:
                if sorted_dct[i] > k:
                    break
                k -= sorted_dct[i]
                len_dct -= 1
            else:
                break
        return len_dct
            