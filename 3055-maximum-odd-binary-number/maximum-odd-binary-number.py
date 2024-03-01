class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        countOnes = 0
        ans = ''
        
        for i in range(len(s)):
            if s[i] == '1':
                countOnes += 1
        

        for i in range(len(s) - 1):
            if i < countOnes-1:
                ans += '1'
            else:
                ans += '0'
        
        ans += '1'

        return ans