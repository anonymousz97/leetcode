class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        res = []
        for query in queries:
            res.append(self.getPathWeight(query[0], query[1], [], graph))
        return res

    def getPathWeight(self, start: str, end: str, visited: list, graph: dict):
        if start not in graph:
            return -1.0

        if end in graph[start]:
            return graph[start][end]

        visited.append(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                productWeight = self.getPathWeight(neighbor, end, visited, graph)
                if productWeight != -1.0:
                    return graph[start][neighbor] * productWeight
        return -1.0



    
    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict[str, dict]:
        graph = {}
        for i, j in zip(equations, values):
            if i[0] not in graph:
                graph[i[0]] = {i[1]: j}
            else:
                graph[i[0]][i[1]] = j
            if i[1] not in graph:
                graph[i[1]] = {i[0]: 1/j}
            else:
                graph[i[1]][i[0]] = 1/j
        return graph
        