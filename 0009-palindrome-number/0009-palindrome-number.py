class Solution:
    def isPalindrome(self, x: int) -> bool:
        backwardString = str(x) [::-1]
        originalString = str(x)
        return originalString == backwardString