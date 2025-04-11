class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        unionSet = {i:i for i in range(len(isConnected))}
        size = {i:1 for i in range(len(isConnected))}

        provinces = set()

        # find the representative of the union find while doing path compression
        def representative(member):
            if unionSet[member] == member:
                return member
            
            unionSet[member] = representative(unionSet[member])
            return unionSet[member]
        
        # union operation
        def union(member1, member2):
            # find the representative of both members
            representative1 = representative(member1)
            representative2 = representative(member2)

            if representative1 != representative2:
                # do the union by rank/size
                if size[representative1] < size[representative2]:
                    unionSet[representative1] = representative2
                    size[representative2] += size[representative1]
                else:
                    unionSet[representative2] = representative1
                    size[representative1] += size[representative2]
        

        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    union(i, j)

        print(unionSet, 'unionSet')
        
        for i in range(len(isConnected)):
            provinces.add(representative(i))

        print(provinces)
        
        return len(provinces)

                