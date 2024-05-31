class Solution:
    def __init__(self):
        self._get()
    def _get(self):
        self.out = []
        for i in range(100000):
            self.out.append(i.bit_count())
    def countBits(self, n: int) -> List[int]:
        return self.out[:n+1]
            
        