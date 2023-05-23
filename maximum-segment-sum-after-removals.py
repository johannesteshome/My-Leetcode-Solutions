class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        Sums = [nums[i] for i in range(len(nums))]
        unionSet = [i for i in range(len(nums))]
        size = [1 for i in range(len(nums))]
        allowed = set()
        answer = [0]
        Max = 0

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
                    Sums[repMember2] += Sums[repMember1]
                else:
                    unionSet[repMember2] = repMember1
                    size[repMember1] += size[repMember2]
                    Sums[repMember1] += Sums[repMember2]

        for i in range(len(nums)-1, 0, -1):
            if removeQueries[i] + 1 in allowed:
                union(removeQueries[i], removeQueries[i] + 1)
            if removeQueries[i] - 1 in allowed:
                union(removeQueries[i], removeQueries[i] - 1)
            
            allowed.add(removeQueries[i])
            Max = max(Max, Sums[find(removeQueries[i])])
            answer.append(Max)
                    
        return answer[::-1]