class Solution:
    def tribonacci(self, n: int) -> int:

        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            print(i)
            print(memo)
            if i == 0:
                memo[i] = 0
                return 0
            
            if i == 1 or i == 2:
                memo[i] = 1
                return 1

            memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
            return memo[i]
        
        return dp(n)
        # print(memo)