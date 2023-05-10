class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)
        answer = []

        def dfs(node, answer):
            if color[node] == 1:
                return False

            if color[node] == 2:
                return True
            
            color[node] = 1

            for children in graph[node]:
            
                res = dfs(children, answer)
            
                if not res:
                    return False
                
            
            color[node] = 2
            answer.append(node)
            return True

        for i in range(len(graph)):
            if color[i] == 0:
                dfs(i, answer)
            
        
        return sorted(answer)