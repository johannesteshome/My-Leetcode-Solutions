class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        first = 0
        for i in range(n):
            # print(ans)
            if i % 7 == 0:
                ans = ans + (first + 1)
                first = first + 1
            else:
                ans = ans + (first + (i % 7))
        
        return ans