class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        dp = [float("inf")] * amount


        for i in range(len(coins)):
            if amount-coins[i] >= 0:
                dp[amount-coins[i]] = 1

        for i in range(amount-1, -1, -1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i - coins[j]] = min(dp[i-coins[j]], dp[i]+1)

        print(dp)
        if dp[0] == float("inf"):
            return -1
        return dp[0]

