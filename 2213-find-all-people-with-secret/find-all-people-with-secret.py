class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
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
                if rep1 == 0:
                    unionSet[rep2] = rep1
                else:
                    unionSet[rep1] = rep2
                
        
        time = defaultdict(list)
        unionSet = {}

        for meeting in meetings:
            time[meeting[2]].append(meeting)
        
        for i in range(n):
            unionSet[i] = i
        
        time = dict(sorted(time.items()))
        union(0, firstPerson)
        print(time)

        
        for k in time:
            for t in time[k]:
              union(t[0], t[1])
            
            for t in time[k]:
                if find(t[0]) != 0:
                    unionSet[t[0]] = t[0]
                if find(t[1]) != 0:
                    unionSet[t[1]] = t[1]

        
        ans = []
        for union in unionSet:
            if find(union) == 0:
                ans.append(union)
        
        return ans