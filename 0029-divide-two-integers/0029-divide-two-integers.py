class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1

        ans = 0
        sign = 1

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        n = abs(dividend)
        d = abs(divisor)

        while n >= d:
            count = 0
            while n > (d << (count + 1)):
                count+=1
            n -= d << count
            ans += 1 << count

        if ans == (1 << 31) and sign == 1:
            return 2**31-1

        return sign * ans
    