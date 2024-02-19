import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if math.log2(n) == int(math.log2(n)):
            return True
        return False
