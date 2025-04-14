class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def power(x, y):
            result = 1
            x %= mod
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % mod
                x = (x * x) % mod
                y //= 2
            return result

        even_count = (n + 1) // 2
        odd_count = n // 2

        return (power(5, even_count) * power(4, odd_count)) % mod