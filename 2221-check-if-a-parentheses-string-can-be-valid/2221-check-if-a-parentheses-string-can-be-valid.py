class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        min_b = max_b = 0 # min_b is the minimum possible open parentheses balance that ensures validity. max_b is the maximum possible open parentheses balance, given the flexibility of unlocked characters.
        for i in range(len(s)):
            is_open = s[i] == '(' # check if the index is opening bracket
            is_unlocked = locked[i] == '0' # check if the index is unlock
            min_b += (-1 if not is_open or is_unlocked else 1) # only add when locked with opening bracket
            max_b += (1 if is_open or is_unlocked else -1) # only minus when locked with closing bracket
            if max_b < 0:
                return False
            min_b = max(min_b, 0)
        return min_b == 0



        