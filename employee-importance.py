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
        adjList = defaultdict(list)
        imptce = {}
        importance = 0
        visited = set()

        for emp in employees:
            adjList[emp.id] = emp.subordinates
            imptce[emp.id] = emp.importance

        # print(imptce)
        # print(adjList)

        def dfs(id, imp):
            nonlocal importance

            importance += imp

            visited.add(id)

            for neighbour in adjList[id]:
                # print(adjList[id], neighbour)
                if neighbour not in visited:
                    # print(imptce)
                    dfs(neighbour, imptce[neighbour])

        dfs(id, imptce[id])
        return importance