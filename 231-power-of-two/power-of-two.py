class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def powerTwo(n):
            if n == 0:
                return False
            elif n == 1:
                return True
            elif n%2 != 0:
                return False
            
            return powerTwo(n/2)
        
        return powerTwo(n)