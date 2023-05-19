class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        unionSet = {i:i for i in range(len(s))}
        unionStr = {i:[s[i]] for i in range(len(s))}
        size = [1 for i in range(len(s))]
        answer = ""

        def find(member):
            if member == unionSet[member]:
                return member

            unionSet[member] = find(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            rep1 = find(member1)
            rep2 = find(member2)

            if rep1 != rep2:
                if size[rep1] < size[rep2]:
                    unionSet[rep1] = rep2
                    size[rep2] += size[rep1]
                    unionStr[rep2].extend(unionStr[rep1])
                else:
                    unionSet[rep2] = rep1
                    size[rep1] += size[rep2]
                    unionStr[rep1].extend(unionStr[rep2])

        for pair in pairs:
            union(pair[0], pair[1])

        # print(unionStr, unionSet)
        for key in unionStr:
            heapify(unionStr[key])

        for i in range(len(s)):
            # print(unionStr[find(i)])
            answer += heappop(unionStr[find(i)])

        return answer