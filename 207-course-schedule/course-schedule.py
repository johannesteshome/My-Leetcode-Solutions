class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = defaultdict(list)
        nodeDegree = [0 for _ in range(numCourses)]
        queue = deque([])

        for node1, node2 in prerequisites:
            adjList[node2].append(node1)
            nodeDegree[node1] += 1
        
        for i in range(len(nodeDegree)):
            if nodeDegree[i] == 0:
                queue.append(i)
        
        # print(nodeDegree, 'nodeDegree', adjList, 'adjList')

        # print(len(queue))

        if not queue:
            return False

        
        while len(queue) > 0:

            node = queue.popleft()

            for child in adjList[node]:

                nodeDegree[child] -= 1

                if nodeDegree[child] == 0:
                    queue.append(child)
        
        
        for i in range(len(nodeDegree)):
            if nodeDegree[i] != 0:
                return False
        
        return True
                

        