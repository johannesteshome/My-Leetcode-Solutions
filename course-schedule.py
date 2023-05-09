class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque()

        for courses in prerequisites:
            adjList[courses[1]].append(courses[0])
            indegree[courses[0]] += 1
        
        # print(indegree, adjList)
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            
            for neighbors in adjList[course]:
                indegree[neighbors] -= 1

                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        
        for ind in indegree:
            if ind != 0:
                return False
        return True