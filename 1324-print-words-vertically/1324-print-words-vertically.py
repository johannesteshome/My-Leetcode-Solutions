class Solution:
    def printVertically(self, s: str) -> List[str]:
        arrStr = s.split()
        
        crossStr = list(itertools.zip_longest(*arrStr, fillvalue =' ' ))
        
        for i in range(len(crossStr)):
            crossStr[i] = "".join(crossStr[i]).rstrip()
        
        return crossStr