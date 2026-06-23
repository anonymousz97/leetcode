

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current_str = ""
        result = []
        def backtrack(cur_str, open, close, n):
            if len(cur_str) == 2 * n:
                result.append(cur_str)
                return 
            if open == n:
                backtrack(cur_str+")", open, close+1, n)
            elif open > close:
                backtrack(cur_str+"(", open+1, close, n)
                backtrack(cur_str+")", open, close+1, n)
            else:
                backtrack(cur_str+"(", open+1, close, n)
        backtrack(current_str, 0,0, n)
        return result

        