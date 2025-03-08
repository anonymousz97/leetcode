class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_v = 99999
        for i in range(len(blocks)- k+1):
            tmp = blocks[i:i+k]
            if [x for x in tmp].count("W") < min_v:
                min_v = [x for x in tmp].count("W")
        return min_v
        