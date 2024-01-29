class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last = 0
        cnt = 0
        for i in timeSeries:
            if last == 0:
                last = i + duration - 1
                cnt += duration
            else:
                if i > last:
                    cnt += duration
                elif i == last:
                    cnt += duration - 1
                else:
                    cnt += i + duration - 1 - last
                last = i + duration - 1   
        return cnt
                    
        