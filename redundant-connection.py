class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionSet = {i:i for i in range(1, len(edges)+1)}
        size = {i:1 for i in range(1, len(edges)+1)}
        # print(unionSet)

        def representative(member):
            if member == unionSet[member]:
                return member
            
            unionSet[member] = representative(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            repMember1 = representative(member1)
            repMember2 = representative(member2)

            if repMember1 != repMember2:
                if size[repMember1] < size[repMember2]:
                    unionSet[repMember1] = repMember2
                    size[repMember2] += size[repMember1]
                else:
                    unionSet[repMember2] = repMember1
                    size[repMember1] += size[repMember2]

        for member1, member2 in edges:
            if representative(member1) == representative(member2):
                return [member1, member2]
            union(member1, member2)