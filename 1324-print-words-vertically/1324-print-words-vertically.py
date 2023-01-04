class Solution:
    def printVertically(self, s: str) -> List[str]:
        arrStr = s.split()
        
        print(arrStr)
        crossStr = list(itertools.zip_longest(*arrStr, fillvalue =' ' ))
        print(crossStr)
        for i in range(len(crossStr)):
            crossStr[i] = "".join(crossStr[i]).rstrip()
        print(crossStr)
        return crossStr