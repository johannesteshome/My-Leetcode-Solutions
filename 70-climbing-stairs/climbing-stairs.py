class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        
        def dp(step):
            if step < 3:
                return step

            if step in memo:
                return memo[step]

            res = dp(step-2) + dp(step - 1)
            memo[step] = res
            return memo[step]

        
        return dp(n)
            