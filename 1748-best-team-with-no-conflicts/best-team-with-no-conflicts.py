class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        combined = list(zip(ages, scores))
        combined = sorted(combined)

        dp = [combined[i][1] for i in range(len(scores))]

        for i in range(len(scores)-1, -1, -1):
            for j in range(i+1, len(scores)):
                if combined[i][0] < combined[j][0]:
                    if combined[i][1] > combined[j][1]:
                        continue
                dp[i] = max(dp[i], dp[j]+combined[i][1])
        
        return max(dp)