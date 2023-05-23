class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parentSet = [set([i]) for i in range(n)]
        size = [1 for i in range(n)]
        unionSet = [i for i in range(n)]
        restricted = defaultdict(set)
        answer = []
        
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
                    parentSet[repMember2].update(parentSet[repMember1])
                else:
                    unionSet[repMember2] = repMember1
                    size[repMember1] += size[repMember2]
                    parentSet[repMember1].update(parentSet[repMember2])

        for x,y in restrictions:
            restricted[x].add(y)
            restricted[y].add(x)

        # print(restricted, parentSet)

        for reqi, reqj in requests:
            notAllowed = set()
            for mem in parentSet[find(reqi)]:
                notAllowed.update(restricted[mem])
            # print(notAllowed, "notallowed", notAllowed.intersection(parentSet[find(reqj)]), parentSet[reqj])
            if len(notAllowed.intersection(parentSet[find(reqj)])) == 0:
                union(reqi, reqj)
                answer.append(True)
            else:
                answer.append(False)
            # print(parentSet)

        return answer