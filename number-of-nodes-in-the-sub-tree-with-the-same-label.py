class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0] * len(labels)
        adjList = defaultdict(list)
        visited = set()

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        print(adjList)

        def dfs(node):
            res = Counter()
            visited.add(node)
            answer[node] = 1

        
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    res += dfs(neighbour)
            
            if not res:
                return Counter(labels[node])
            
            count = Counter(labels[node])
            count += res
            answer[node] = count[labels[node]]
            return count

        dfs(0)
        
        return answer