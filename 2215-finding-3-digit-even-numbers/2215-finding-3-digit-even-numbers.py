from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = {
            100*a + 10*b + c
            for a, b, c in permutations(digits, 3)
            if a != 0 and c % 2 == 0
        }
        return sorted(result)