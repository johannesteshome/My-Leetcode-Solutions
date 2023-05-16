class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        visited = set()
        answer = []

        for from_, to_ in adjacentPairs:
            adjList[from_].append(to_)
            adjList[to_].append(from_)
            indegree[from_] += 1
            indegree[to_] += 1

        def dfs(node):
            answer.append(node)
            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in indegree:
            if indegree[node] == 1:
                dfs(node)
                break
        
        return answer