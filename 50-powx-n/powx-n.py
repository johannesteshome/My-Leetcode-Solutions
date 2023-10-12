class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        c = 1
        tn = abs(n)
        for _ in range(32):
            if tn & c != 0:
                result *= x
            x *= x
            c <<= 1
        if n < 0:
            return 1/result
        return result
        # while exponent > 0:
        #     if exponent & 1:
        #         result *= base
        #     base *= base
        #     exponent >>= 1
        # return result