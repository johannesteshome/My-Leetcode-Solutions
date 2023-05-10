class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = []
        adjList = defaultdict(list)
        indegree = [0] * n

        for edge in edges:
            adjList[edge[1]].append(edge[0])
            indegree[edge[1]] += 1

        print(adjList, indegree)

        def bfs():
            while queue:
                level = len(queue)
                
                for _ in range(level):
                    node = queue.popleft()

                    if node in adjList:
                        for children in adjList[node]:
                            if children not in visited:
                                queue.append(children)
                                ans.append(children)
                                visited.add(children)
                    
            
            return sorted(ans)

        
        for i in range(n):
            if indegree[i] == 0:
                answer.append([])
            else:
                queue = deque([i])
                ans = []
                visited = set()
                answer.append(bfs())
        
        return answer