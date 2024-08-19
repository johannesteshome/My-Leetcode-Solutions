class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = []
        answer = []

        for i in range(len(score)):
            answer.append(0)

        for i in range(len(score)):
            ranks.append((score[i], i))
        
        ranks = sorted(ranks, reverse=True)
        
        for i in range(len(ranks)):
            if(i == 0):
                answer[ranks[i][1]] = "Gold Medal"
            elif(i == 1):
                answer[ranks[i][1]] = "Silver Medal"
            elif(i == 2):
                answer[ranks[i][1]] = "Bronze Medal"
            else:
                answer[ranks[i][1]] = str(i+1)
        
        return answer
