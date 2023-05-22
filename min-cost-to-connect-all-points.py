class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        unionSet = {}
        size = {}

        def manDist(point1, point2):
            return abs(abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))
        
        def find(member):
            if member == unionSet[member]:
                return member
            
            unionSet[member] = find(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            repMember1 = find(member1)
            repMember2 = find(member2)

            if repMember1 != repMember2:
                if size[repMember1] < size[repMember2]:
                    unionSet[repMember1] = repMember2
                    size[repMember2] += size[repMember1]
                else:
                    unionSet[repMember2] = repMember1
                    size[repMember1] += size[repMember2]

        for x,y in points:
            unionSet[(x,y)] = (x,y)
            size[(x,y)] = 1

        edges = []

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((manDist(points[i], points[j]), (points[i][0], points[i][1]), (points[j][0], points[j][1])))
        
        edges.sort()

        answer = 0
        path = 0

        for length, u, v in edges:
            if find(u) != find(v):
                union(u,v)
                answer += length
                path += 1
            
            if path == len(points) - 1:
                break
        
        return answer