class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        unionSet = {}
        size = {}


        for i in range(len(source)):
            unionSet[i] = i
            size[i] = 1

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

        for swaps in allowedSwaps:
            union(swaps[0], swaps[1])

        parentSet = defaultdict(list)
        # print(unionSet)

        for union in unionSet:
            parentSet[find(union)].append(source[union])
        
        for key in parentSet:
            parentSet[key] = Counter(parentSet[key])

        answer = 0
        
        for i in range(len(target)):
            if target[i] in parentSet[find(i)] and parentSet[find(i)][target[i]] != 0:
                parentSet[find(i)][target[i]] -= 1
                continue
            answer += 1

        return answer