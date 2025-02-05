class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        a = b = ""
        for i, j in zip(s1, s2):
            if i != j:
                cnt += 1
                a += i
                b += j
        if cnt == 1 or cnt > 2:
            return False

        if a == b[::-1]:        
            return True
        return False 
        