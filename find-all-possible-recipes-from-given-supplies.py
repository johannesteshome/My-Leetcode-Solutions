class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplySet = set()
        adjList = defaultdict(list)
        # indegree = [0] * len(ingredients)
        indegree = defaultdict(int)
        queue = deque()
        answer = []

        for supply in supplies:
            supplySet.add(supply)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplySet:
                    adjList[ingredients[i][j]].append(recipes[i])
                    indegree[recipes[i]] += 1
        
        # print(adjList, indegree)

        for i in range(len(recipes)):
            if indegree[recipes[i]] == 0:
                queue.append(recipes[i])

        while queue:
            node = queue.popleft()
            answer.append(node)

            for neighbors in adjList[node]:
                indegree[neighbors] -= 1

                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        
        return answer