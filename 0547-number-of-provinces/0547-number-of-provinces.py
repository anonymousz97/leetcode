class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = [False] * len(isConnected)
        count = 0

        def dfs(u):
            for v in range(len(isConnected)):
                if isConnected[u][v] == 1 and visited[v] == False:
                    visited[v] = True
                    dfs(v)
        
        for i in range(len(isConnected)):
            if visited[i] == False:
                count += 1
                visited[i] == True
                dfs(i)
        
        return count
