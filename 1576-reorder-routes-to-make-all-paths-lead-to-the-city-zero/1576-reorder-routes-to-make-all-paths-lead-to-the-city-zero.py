from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        directed_edges = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            directed_edges.add((a, b))
        
        self.changes = 0
        visited = set()
    
        def dfs(city):
            visited.add(city)
            for neighbor in graph[city]:
                if neighbor in visited:
                    continue
                if (city, neighbor) in directed_edges:
                    self.changes += 1
                dfs(neighbor)
        dfs(0)
        return self.changes


        