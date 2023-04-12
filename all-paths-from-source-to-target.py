class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        target = len(graph) - 1
        def dfs(node, path):
            # print(node)
            if node == target:
                answer.append(path)
                return
            
            for neighbour in graph[node]:
                dfs(neighbour, path+[neighbour])
        

        dfs(0, [0])

        return answer