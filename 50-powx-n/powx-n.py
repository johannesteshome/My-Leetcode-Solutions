class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        
        def pow(power):
            if power == 1:
                return x

            ans = pow(power // 2)
            ans *= ans
            if power % 2:
                ans *= x
            
            return ans
        
        if n < 0:
            ret = pow(-n)
            ans = 1/ret
        else:
            ans = pow(n)
        
        return ans
            
