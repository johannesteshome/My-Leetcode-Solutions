class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        unionSet = {i:i for i in range(1, n+1)}
        size = {i:1 for i in range(1, n+1)}
        distance = {i:float("inf") for i in range(1, n+1)}
        # print(unionSet)
        print(unionSet, size, distance)

        def representative(member):
            if member == unionSet[member]:
                return member
            
            unionSet[member] = representative(unionSet[member])
            return unionSet[member]

        def union(member1, member2, distances):
            repMember1 = representative(member1)
            repMember2 = representative(member2)

        
            if size[repMember1] < size[repMember2]:
                unionSet[repMember1] = repMember2
                size[repMember2] += size[repMember1]
                distance[repMember2] = min(distance[repMember1], distance[repMember2], distances)
            else:
                unionSet[repMember2] = repMember1
                size[repMember1] += size[repMember2]
                distance[repMember1] = min(distance[repMember1], distance[repMember2], distances)
        
        for city1, city2, d in roads:
            union(city1, city2, d)
        
        return distance[representative(1)]