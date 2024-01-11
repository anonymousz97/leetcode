class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        lst_vowels = ['a','e','i','o','u']
        init = sum([s[:k].count(x) for x in lst_vowels])
        max_v = init
        for i in range(k, len(s)):
            if s[i] in lst_vowels:
                init += 1
            if s[i-k] in lst_vowels:
                init -= 1
            if max_v < init:
                max_v = init
        return max_v