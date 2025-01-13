from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if x % 2 else 2 for x in Counter(s).values()) # if counter is odd so 1 remain after remove and if even so 2 left (since cannot remove the last pair)