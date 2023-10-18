class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        unionSet = {}
        def find(member):
            # print(member)
            if member == unionSet[member]:
                return member

            unionSet[member] = find(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            # print(member1, member2, "members")
            rep1 = find(member1)
            rep2 = find(member2)

            if rep1 != rep2:
                if size[rep1] < size[rep2]:
                    unionSet[rep1] = rep2
                    size[rep2] += size[rep1]
                else:
                    unionSet[rep2] = rep1
                    size[rep1] += size[rep2]

        unionSet = {}
        size = {}

        for s in strs:
            unionSet[s] = s
            size[s] = 1
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                diff = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        diff += 1
                if diff <= 2:
                    union(strs[i], strs[j])
        
        print(unionSet)
        ans = defaultdict(list)

        for union in unionSet:
            ans[find(unionSet[union])].append(union)
        
        return len(ans)

        return 9