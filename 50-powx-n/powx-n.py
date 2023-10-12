class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        tn = abs(n)
        while tn > 0:
            if tn & 1:
                result *= x
            x *= x
            tn >>= 1
        if n < 0:
            return 1/result
        return result