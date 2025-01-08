class Solution:
    def check(self, wordA: str, wordB: str) -> int:
        return int(wordB.startswith(wordA) and wordB.endswith(wordA))
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        s = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words), 1):
                s += self.check(words[i], words[j])
        return s
        