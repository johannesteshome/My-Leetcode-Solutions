class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newString = ""
        firstIndex = 0
        for i in range(len(spaces)):
            newString = newString + s[firstIndex:spaces[i]] + " "
            firstIndex = spaces[i]
            
        newString = newString + s[firstIndex:]
        return newString
        