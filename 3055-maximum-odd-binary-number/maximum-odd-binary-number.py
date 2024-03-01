class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        countOnes = s.count('1')
        n = len(s)

        return '1' * (countOnes - 1) + '0' * (n - countOnes) + '1'