from collections import deque 

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        n = len(senate)
        dequeR = deque([idx for idx in range(n) if senate[idx]=='R'])
        dequeD = deque([idx for idx in range(n) if senate[idx]=='D'])
        
        while len(dequeR) > 0 and len(dequeD) > 0:
            a = dequeR.popleft()
            b = dequeD.popleft()
            if a < b:
                dequeR.append(n+a)
            else:
                dequeD.append(n+b)
        
        if len(dequeR) == 0:
            return "Dire"
        return "Radiant"
        