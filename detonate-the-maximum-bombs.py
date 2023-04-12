class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited = set()
        adjList = defaultdict(list)
        Max = 0
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                distance = sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)
                # print(distance)
                if i != j and bombs[i][2] >= distance:
                    adjList[i].append(j)
        
        def dfs(b):

            visited.add(b)

            for neighbours in adjList[b]:
                # print(adjList[b])
                if neighbours not in visited:
                    dfs(neighbours)

        
        print(adjList)
        for adj in range(len(bombs)):
            dfs(adj)
            print(visited)
            Max = max(Max, len(visited)) 
            visited.clear()           

        return Max