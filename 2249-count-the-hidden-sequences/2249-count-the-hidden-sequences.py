class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = 0
        maxi = 0
        mini = 0
        for i in differences:
            x += i
            maxi = max(maxi, x)
            mini = min(mini, x)
        return max(0, upper - lower - maxi + mini + 1)
        