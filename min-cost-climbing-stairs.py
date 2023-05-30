class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        if len(cost) == 2:
            return min(cost)

        def dp(i):
            if i in memo:
                return memo[i]
            if i < 2:
                memo[i] = cost[i]
                return cost[i]
            
            memo[i] = cost[i] + min(dp(i-1), dp(i-2))
            return memo[i]
        
        dp(len(cost) - 1)
        return min(memo[len(cost) - 1], memo[len(cost) - 2])