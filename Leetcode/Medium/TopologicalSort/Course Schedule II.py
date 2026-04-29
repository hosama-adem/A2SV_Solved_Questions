class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]

        queue = deque()
        order = []
        for co,pre  in prerequisites:
            graph[pre].append(co)
            incoming[co] += 1
        
        for cou in range(numCourses):
            if incoming[cou] == 0:
                queue.append(cou)
        

        while queue:
            course = queue.popleft()
            order.append(course)

            for nigh in graph[course]:
                incoming[nigh] -= 1
                if incoming[nigh] == 0:
                    queue.append(nigh)
        
        if len(order) != numCourses:
            return []
        
        return order

