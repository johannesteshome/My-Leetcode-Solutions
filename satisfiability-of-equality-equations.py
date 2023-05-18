class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unionSet = {}
        size = {}

        for equation in equations:
            if equation[0] not in unionSet:
                unionSet[equation[0]] = equation[0]
                size[equation[0]] = 1
            if equation[-1] not in unionSet:
                unionSet[equation[-1]] = equation[-1]
                size[equation[-1]] = 1

        print(unionSet, size)
        def representative(member):
            if member == unionSet[member]:
                return member
            
            unionSet[member] = representative(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            repMember1 = representative(member1)
            repMember2 = representative(member2)
            
            if size[repMember1] < size[repMember2]:
                unionSet[repMember1] = repMember2
                size[repMember2] += size[repMember1]
            else:
                unionSet[repMember2] = repMember1
                size[repMember1] += size[repMember2]

        for equation in equations:
            if equation[1] == "=":
                union(equation[0], equation[-1])
        
        for equation in equations:
            if equation[1] == "!":
                if representative(equation[0]) == representative(equation[-1]):
                    return False

        return True