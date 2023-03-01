class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n < 0:
                return 1 / power(x, -n)
            elif n%2 == 1:
                return x*power(x,n-1)
            return power(x*x, n/2)

        return power(x,n)