class Solution:
    def largestGoodInteger(self, num: str) -> str:
        p1 = 0
        p2 = 2

        Max = float("-inf")
        
        while p2 < len(num):
            if len(set(num[p1:p2+1])) == 1:
                  Max = max(Max, int(num[p1]))
            p1 += 1
            p2 += 1
            # print(num[p1:p2+1], p1, p2)

        if Max == float("-inf"):
          return ""
        s = ""
        for i in range(3):
          s += str(Max)
        
        return s