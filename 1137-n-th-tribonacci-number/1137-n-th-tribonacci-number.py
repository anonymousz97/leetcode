class Solution:
    def __init__(self):
        self.lst = [0,1,1]
        for i in range(36):
            self.lst.append(self.lst[-1]+self.lst[-2]+self.lst[-3])
    
    def tribonacci(self, n: int) -> int:
        return self.lst[n]
        