class Solution:
    def reverseVowels(self, s: str) -> str:
        a = [x for x in s if x in ['a','A','e','E','i','I','o','O','u','U']]
        res = ""
        for i in s:
            if i not in ['a','A','e','E','i','I','o','O','u','U']:
                res += i
            else:
                res += a[-1]
                a = a[:-1]
        return ''.join(x for x in res)