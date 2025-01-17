class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        a = derived[0]
        for i in derived[1:]:
            a ^= i
        return a == 0
        