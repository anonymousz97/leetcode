class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1] * 45
        a[0] = 1
        a[1] = 2
        for i in range(2,45,1):
            a[i] = a[i-2] + a[i-1]
        return a[n-1]
        