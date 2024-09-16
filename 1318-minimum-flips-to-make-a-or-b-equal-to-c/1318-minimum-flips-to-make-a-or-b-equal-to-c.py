import math
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        max_n = int(math.log2(max(a, b, c))) + 1
        rep_a = self.get_bin(a, max_n)
        rep_b = self.get_bin(b, max_n)
        rep_c = self.get_bin(c, max_n)
        cnt = 0
        for i in range(len(rep_c)-1, -1, -1):
            if rep_c[i] == "0":
                if rep_a[i] == "1":
                    cnt += 1
                if rep_b[i] == "1":
                    cnt += 1
            else:
                if rep_a[i] == "0" and rep_b[i] == "0":
                    cnt += 1
        return cnt
    
    def get_bin(self, x, n=0):
        return format(x, 'b').zfill(n)
        