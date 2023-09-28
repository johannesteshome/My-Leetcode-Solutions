class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        length = len(satisfaction)
        print(satisfaction)

        dp = [[0 for _ in range(length)] for _ in range(length)]

        for i in range(length):
            for j in range(length):
                if i - 1 < 0 or j-1 < 0:
                    num = 0
                else:
                    num = dp[i-1][j-1] 
                dp[i][j] = ((i+1) * satisfaction[j]) + num
        
        Max = float("-inf")

        for i in range(length):
            Max = max(Max, dp[length-1][i])
        
        for i in range(length):
            Max = max(Max, dp[i][length-1])
        
        if Max < 0:
            return 0
        return Max
