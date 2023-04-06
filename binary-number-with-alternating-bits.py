class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & (1<<0)
        n = n >> 1
        
        while n > 0:
            if n & (1<<0) == prev:
                return False
            prev = n & (1<<0)
            n = n >> 1
        return True