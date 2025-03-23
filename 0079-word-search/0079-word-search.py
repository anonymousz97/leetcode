class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word

        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self, x: int, y: int, index: int) -> bool:
        if index == len(self.word):
            return True

        if (x < 0 or x >= self.rows or
            y < 0 or y >= self.cols or
            self.board[x][y] != self.word[index]):
            return False

        temp = self.board[x][y]
        self.board[x][y] = '#'

        found = (
            self.dfs(x+1, y, index+1) or
            self.dfs(x-1, y, index+1) or
            self.dfs(x, y+1, index+1) or
            self.dfs(x, y-1, index+1)
        )
        self.board[x][y] = temp
        return found
