class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = ceil(stoneSum / 2)

        memo = {}

        def dp(i, Sum):
            if Sum >= target or i == len(stones):
                return abs(Sum - (stoneSum - Sum))

            state = (i, Sum)

            if state in memo:
                return memo[state]
            
            memo[state] = min(dp(i+1, Sum + stones[i]), dp(i+1, Sum))
            return memo[state]        

        return dp(0,0)
