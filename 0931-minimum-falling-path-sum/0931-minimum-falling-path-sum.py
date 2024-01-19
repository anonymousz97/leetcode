class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        best_r = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
        best_r[-1] = matrix[-1]
        for i in range(len(matrix) - 2, -1, -1):
            for j in range(len(matrix)):
                if j == 0:
                    best_r[i][j] = min(best_r[i+1][j], best_r[i+1][j+1]) + matrix[i][j]
                elif j == len(matrix) - 1:
                    best_r[i][j] = min(best_r[i+1][j], best_r[i+1][j-1]) + matrix[i][j]
                else:
                    best_r[i][j] = min(best_r[i+1][j], best_r[i+1][j+1], best_r[i+1][j-1]) + matrix[i][j]
        for i in range(len(best_r)):
            for j in range(len(best_r)):
                print(best_r[i][j],sep=' ')
            print("\n")
        return min(best_r[0])
                
            
        