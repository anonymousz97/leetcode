class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        tmp = [self.parseTime(x) for x in timePoints]
        tmp.append(tmp[0]+1440)
        min_diff = 2000
        for i in range(1, len(tmp)):
            if tmp[i] - tmp[i-1] < min_diff:
                min_diff = (tmp[i] - tmp[i-1])
        return min_diff
    
    def parseTime(self, timepoint: str):
        p = timepoint.split(":")
        return int(p[0]) * 60 + int(p[1])
        