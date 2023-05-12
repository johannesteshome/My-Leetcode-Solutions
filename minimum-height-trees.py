class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
      
        adjList = defaultdict(set)
        unvisited = n
        queue = deque()

        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])

        for node in adjList:
            if len(adjList[node]) == 1:
                unvisited -= 1
                queue.append(node)
        
        while unvisited != 0:
            for _ in range(len(queue)):
                node = queue.popleft()

                for children in adjList[node]:
                    adjList[children].discard(node)
                    if len(adjList[children]) == 1:
                        queue.append(children)
                        unvisited -= 1
        
        return queue