class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        unionSet = {}
        answer = ""

        for i in range(len(s1)):
            unionSet[s1[i]] = s1[i]
            unionSet[s2[i]] = s2[i]

        # print(unionSet)
        # print(unionSet['p'])

        def representative(member):
            print(member, unionSet[member])
            if member == unionSet[member]:
                return member
            
            unionSet[member] = representative(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            repMember1 = representative(member1)
            repMember2 = representative(member2)

            if repMember1 != repMember2:
                if repMember1 < repMember2:
                    unionSet[repMember2] = repMember1
                else:
                    unionSet[repMember1] = repMember2
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        for i in range(len(baseStr)):
            if baseStr[i] in unionSet:
                answer += representative(baseStr[i])
            else:
                answer += baseStr[i]
        
        return answer