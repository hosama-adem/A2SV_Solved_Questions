class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def bfs(graph):
            res = []
            queue = deque([[0]])
            target = len(graph) - 1

            while queue:
                temp = queue.popleft()
                if temp[-1] == target:
                    res.append(temp)
                else:
                    for nigh in graph[temp[-1]]:
                        queue.append(temp + [nigh])
            
            return res
        
        return bfs(graph)
