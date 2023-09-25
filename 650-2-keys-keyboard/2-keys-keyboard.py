class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def dp(N, steps, clipboard):
            if N >= n:
                if N == n:
                    return steps
                else:
                    return float("inf")
            state = (N, steps)
            
            memo[state] = min(dp(N+clipboard, steps+1, clipboard), dp(N+N, steps+2, N))
            return memo[state]
        
        if n == 2:
            return 2
        elif n == 1:
            return 0
        
        return dp(2,2, 1)
        