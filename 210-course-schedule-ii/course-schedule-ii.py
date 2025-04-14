class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque([])
        order = []
        
        for courses in prerequisites:
            adjList[courses[1]].append(courses[0])
            indegree[courses[0]] += 1
        
        for i in range(len(indegree)):

            if indegree[i] == 0:
                queue.append(i)
        

        while queue:

            node = queue.popleft()
            
            if indegree[node] == 0:
                order.append(node)
            
            for child in adjList[node]:

                indegree[child] -= 1

                if indegree[child] == 0:
                    queue.append(child)
        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return []
        
        return order

