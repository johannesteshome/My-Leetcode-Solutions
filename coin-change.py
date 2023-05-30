class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        # coins = sorted(coins, reverse=True)
        def dp(i, Sum):

            state = (i, Sum)

            if state in memo:
                return memo[state]
            
            if Sum == 0:
                return 0
            
            if i == len(coins):
                return inf

            answer = dp(i+1, Sum)

            if Sum - coins[i] >= 0:
                answer = min(answer, dp(i, Sum-coins[i]) + 1)
            
            memo[state] = answer
            return answer
        
        ans = dp(0, amount)

        if ans == inf:
            return -1
        return ans