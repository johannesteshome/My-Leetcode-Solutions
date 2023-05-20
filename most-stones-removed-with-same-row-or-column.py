class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        unionSet = {(stones[i][0], stones[i][1]):(stones[i][0], stones[i][1]) for i in range(len(stones))}
        size = {(stones[i][0], stones[i][1]):1 for i in range(len(stones))}

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

        # print(unionSet, "ünionSet")

        for i in range(len(stones)-1):
            for j in range(i+1, len(stones)):
                # print(stones[i], stones[j])
                if stones[i][0] == stones[j][0]:
                    # print(stones[i], stones[j], "here row")
                    union((stones[i][0], stones[i][1]), (stones[j][0], stones[j][1]))
                if stones[i][1] == stones[j][1]:
                    # print(stones[i], stones[j], "here col")
                    union((stones[i][0], stones[i][1]), (stones[j][0], stones[j][1]))
                    
    
        # rows = defaultdict(list)
        # cols = defaultdict(list)

        # for stone in stones:
        #     rows[stone[0]].append(stone)
        #     cols[stone[1]].append(stone)
        # # print(rows, cols, "rows&cols")

        
        # for stone in stones:
        #     if stone[0] in rows:
        #         for s in rows[stone[0]]:
        #             union((stone[0], stone[1]), (s[0], s[1]))
        #     if stone[1] in cols:
        #         for s in cols[stone[1]]:
        #             union((stone[0], stone[1]), (s[0], s[1]))
        
        unions = defaultdict(int)
        for key in unionSet:
            unions[find(key)] += 1
        
        # print(unions)

      
        # print(unionSet, "unionSet")
        return sum(unions.values()) - len(unions)