class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        if n == 0:
            return 0
        
        # Initialize dp array with size n+1. dp[i] represents the maximum points starting from question i.
        dp = [0] * (n + 1)  

        for i in range(n-1, -1, -1):
            solve = questions[i][0]
            brainpower = questions[i][1]

            if i + brainpower < n:
                next_i = i + brainpower + 1
                solve += dp[next_i]

            skip = dp[i+1]
            
            dp[i] = max(solve, skip)
        
        return dp[0]
            