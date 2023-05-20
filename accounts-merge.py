class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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
        user = {}
        for account in accounts:
            for ac in account[1:]:
                unionSet[ac] = ac
                size[ac] = 1
                user[ac] = account[0]

        
        for account in accounts:
            for i in range(2, len(account)):
                union(account[1], account[i])
        
        # print(unionSet, "unionSet")
        # print(user, "user")

        answer = defaultdict(list)
        ans = []

        for union in unionSet:
            answer[find(union)].append(union)

        # print(answer)

        for key, values in answer.items():
            ans.append([user[key]])
            ans[-1].extend(sorted(answer[key]))

        return ans