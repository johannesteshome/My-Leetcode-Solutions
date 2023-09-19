class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return cost[n]
            elif n == 1:
                memo[n] = min(cost[1], cost[1] + cost[0])
            else:
                memo[n] = min(dp(n-1), dp(n-2)) + cost[n]
            return memo[n]
            
        
        return min(dp(len(cost)-1), dp(len(cost)-2))
        