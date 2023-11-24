class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dif = []
        answer = 0

        for index, cost in enumerate(costs):
            dif.append([abs(cost[0] - cost[1]), index])
        
        dif = sorted(dif, reverse = True)
        # print(dif)

        cityA = 0
        cityB = 0
        answer = 0

        for d, index in dif:
            if costs[index][0] < costs[index][1]:
                if cityA < len(costs) // 2:
                    answer += costs[index][0]
                    cityA += 1
                    # print(cityA, "a")
                else:
                    answer += costs[index][1]
                    cityB += 1
            else:
                if cityB < len(costs) // 2:
                    answer += costs[index][1]
                    cityB += 1
                    # print(cityB, "b")
                else:
                    answer += costs[index][0]
                    cityA += 1

        return answer
        