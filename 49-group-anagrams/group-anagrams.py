class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrings = []
        ans = []

        for i in range(len(strs)):
            newS = sorted(strs[i])
            sortedStrings.append((newS, strs[i]))
        
        sortedStrings.sort()

        ans.append([sortedStrings[0][1]])

        for i in range(1, len(sortedStrings)):
            if sortedStrings[i][0] == sortedStrings[i-1][0]:
                ans[-1].append(sortedStrings[i][1])
            if sortedStrings[i][0] != sortedStrings[i-1][0]:
                ans.append([sortedStrings[i][1]])
        
        return ans