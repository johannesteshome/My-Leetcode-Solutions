class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        answer = []
        queue = deque()
        indegree = [0] * numCourses

        for prerequisite in prerequisites:
            adjList[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        # print(adjList, indegree)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            answer.append(course)

            for neighbors in adjList[course]:
                indegree[neighbors] -= 1

                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        
        for ind in indegree:
            if ind != 0:
                return []
        return answer