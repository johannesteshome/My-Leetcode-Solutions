class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        outdegree = [0 for i in range(numCourses)]
        answer = []

        for first, then in prerequisites:
            adjList[first].append(then)
            outdegree[first] += 1
        
        def dfs(node):
            nonlocal course
            visited.add(node)

            if node == course:
                return True

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    res = dfs(neighbor)
                    
                    if res:
                        return True
        
        for index, query in enumerate(queries):
            visited = set()
            course = query[1]
            if outdegree[query[0]] == 0:
                answer.append(False)
            else:
                answer.append(dfs(query[0]))
        
        return answer