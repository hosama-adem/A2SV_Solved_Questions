class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #constructing the graph 
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            for nigh in graph[node]:
                if nigh not in visited:
                    if dfs(nigh, visited):
                        return True
            
            return False
        
        return dfs(source, visited)
