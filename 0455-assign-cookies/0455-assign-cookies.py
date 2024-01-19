class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        cnt = 0
        for i in g:
            for idx, j in enumerate(s):
                if j >= i:
                    del s[idx]
                    cnt += 1
                    break
        return cnt
                    
                    
        