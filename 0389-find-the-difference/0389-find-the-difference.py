class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        strMap = Counter(s)
        # print(strMap)
        for i in range(len(t)):
            if(t[i] in strMap and strMap[t[i]] != 0):
                strMap[t[i]] -= 1
            else:
                return t[i]