class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n #color of the nodes 0 to n-1 nodes
        
        def dfs(node):
            for nigh in graph[node]:
                if color[nigh] == -1:
                    color[nigh] = 1 - color[node]
                    if not dfs(nigh):
                        return False
                elif color[nigh] == color[node]:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
            
        return True
            
