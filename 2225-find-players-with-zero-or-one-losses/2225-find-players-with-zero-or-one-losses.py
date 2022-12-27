class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        winnerList = []
        loserList = []
        for match in matches:
            if(match[0] in winners):
                winners[match[0]] += 1
            else:
                winners[match[0]] = 1
            if(match[1] in losers):
                losers[match[1]] += 1
            else:
                losers[match[1]] = 1
                
        for winner in winners:
            if(winner not in losers):
                winnerList.append(winner)
                
        for loser in losers:
            if(losers[loser] == 1):
                loserList.append(loser)
               
        answer = []
        answer.append(sorted(winnerList))        
        answer.append(sorted(loserList))
        return answer