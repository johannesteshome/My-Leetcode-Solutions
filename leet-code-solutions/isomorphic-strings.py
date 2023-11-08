class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        sIndex = []
        tMap = {}
        tIndex = []
        print(sMap.values(),tMap.values())

        for index, st in enumerate(s):
            if st in sMap:
                sIndex.append(sMap[st])
            else:
                sMap[st] = index
                sIndex.append(sMap[st])
        
        for indexT, ts in enumerate(t):
            if ts in tMap:
                tIndex.append(tMap[ts])
            else:
                tMap[ts] = indexT
                tIndex.append(tMap[ts])


        if sIndex == tIndex:
            return True
        else:
            return False
    
        # print(sMap,tMap)