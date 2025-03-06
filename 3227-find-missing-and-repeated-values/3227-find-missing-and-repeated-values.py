class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        tmp = [0 for x in range(len(grid) ** 2)]
        for i in grid:
            for j in i:
                tmp[j-1] += 1
        return [tmp.index(2) + 1, tmp.index(0) + 1]
        