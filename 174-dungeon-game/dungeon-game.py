class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if dungeon[i][j] < 0:
                    if dp[i+1][j] == 0 and dp[i][j+1] == 0:
                        dp[i][j] = dungeon[i][j]
                    else:
                        if i+1 == m:
                            dp[i][j] = dungeon[i][j] + dp[i][j+1]
                        elif j+1 == n:
                            dp[i][j] = dungeon[i][j] + dp[i+1][j]
                        else:
                            dp[i][j] = max(dungeon[i][j] + dp[i+1][j], dungeon[i][j]+dp[i][j+1])
                else:
                    if dp[i+1][j] == 0 and dp[i][j+1] == 0:
                        dp[i][j] = 0
                    else:
                        if dungeon[i][j] >= abs(dp[i+1][j]):
                            num1 = 0
                        else:
                            num1 = dungeon[i][j] + dp[i+1][j]
                        if dungeon[i][j] >= abs(dp[i][j+1]):
                            num2 = 0
                        else:
                            num2 = dungeon[i][j] + dp[i][j+1]
                        
                        if i+1 == m or j+1 == n:
                            dp[i][j] = min(num1, num2)
                        else:
                            dp[i][j] = max(num1, num2)
        
        print(dp)
        return abs(dp[0][0]) + 1

        