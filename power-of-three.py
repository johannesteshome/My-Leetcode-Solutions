class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powerThree(n):
            print(n)
            if n == 0:
                return False
            elif n == 1:
                return True
            elif n%3 != 0:
                return False
            else:
                return powerThree(n//3)        
        return powerThree(n)