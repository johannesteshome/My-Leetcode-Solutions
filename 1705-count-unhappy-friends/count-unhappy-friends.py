class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pairDict = {}
        for pair in pairs:
            pairDict[pair[0]] = pair[1]
            pairDict[pair[1]] = pair[0]
        
        count = 0

        for p in pairDict:
            # if pairDict[p] != preferences[p][0]:
            for i in range(preferences[p].index(pairDict[p])):
                curr = preferences[p]
                if preferences[curr[i]].index(p) < preferences[curr[i]].index(pairDict[curr[i]]):
                    count += 1 
                    break
        return count
        