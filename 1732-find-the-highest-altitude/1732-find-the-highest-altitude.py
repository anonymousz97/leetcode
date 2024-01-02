class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        pos = 0
        for i in gain:
            pos += i
            if pos > max_altitude:
                max_altitude = pos
        return max_altitude