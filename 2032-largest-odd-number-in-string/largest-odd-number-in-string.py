class Solution:
    def largestOddNumber(self, num: str) -> str:
        found = False
        ans = ""
        for i in range(len(num) - 1, -1, -1):
            if not found and int(num[i]) % 2 != 0:
                ans += num[i]
                found = True
            elif found:
                ans += num[i]
        
        return ans[::-1]