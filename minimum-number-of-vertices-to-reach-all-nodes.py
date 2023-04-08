class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:


        # adjList = defaultdict(list)
        # visited = set()
        # answer = []

        # for i in range(n):
        #     adjList[i] = []

        # def nextNodes(vertex):
        #     if vertex not in visited:
        #         visited.add(vertex)

        #     if len(adjList[vertex]) == 0:
        #         return
            
        #     for vertices in adjList[vertex]:
        #         # print(vertices)
        #         nextNodes(vertices)

        # for edge in edges:
        #     adjList[edge[0]].append(edge[1])
        
        # visits = []
        # # print(adjList)
        # for key in adjList:
        #     if key not in visited:
        #         answer.append(key)
        #         nextNodes(key)
        

        # def nextNodes(vertex):
        #     if vertex not in visited:
        #         visited.add(vertex)

        #     if len(adjList[vertex]) == 0:
        #         return
            
        #     for vertices in adjList[vertex]:
        #         nextNodes[vertices]

        # return answer

        in_degree = [0] * n

        for u, v in edges:
            in_degree[v] += 1

        result = []
        for i in range(n):
            if in_degree[i] == 0:
                result.append(i)

        return result