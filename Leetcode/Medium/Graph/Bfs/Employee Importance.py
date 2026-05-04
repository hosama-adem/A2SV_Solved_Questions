"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(employee, start):
            #construct map for emp
            visited = {e.id: e for e in employee}
            queue = deque([start])
            res = 0

            #until the queue not exist add impo and reach the sub
            while queue:
                current_id = queue.popleft()
                emp = visited[current_id]
                res += emp.importance

                for sub in emp.subordinates:
                    queue.append(sub)
            
            return res

        return dfs(employees, id)
