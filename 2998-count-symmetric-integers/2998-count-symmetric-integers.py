class Solution:
    def symmetric(self, x):
        a = len(x)
        if a % 2 == 1:
            return False
        l = 0
        r = 0
        for i in range(a//2):
            l += int(x[i])
            r += int(x[a-1-i])
        if l == r:
            return True
        return False


    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high+1):
            if self.symmetric(str(i)):
                cnt += 1
        return cnt

        