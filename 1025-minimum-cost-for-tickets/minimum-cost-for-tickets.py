class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366

        for i in range(1, 366):
            if i in days:
                if i - 7 < 0:
                    weekBefore = 0
                else:
                    weekBefore = i-7
                if i - 30 < 0:
                    monthBefore = 0
                else:
                    monthBefore = i - 30
                
                dp[i] = min(dp[i-1] + costs[0], dp[weekBefore] + costs[1], dp[monthBefore] + costs[2])
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]


        