class Solution:
    def fib(self, n: int) -> int:
        mem = defaultdict(int)

        def fibo(n):
            if n == 0 or n==1:
                return n
            elif n not in mem:
                mem[n] = fibo(n-1) + fibo(n-2)
            return mem[n]
        
        return fibo(n)