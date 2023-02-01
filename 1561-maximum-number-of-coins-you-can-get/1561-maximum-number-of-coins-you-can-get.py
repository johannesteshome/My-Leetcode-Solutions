class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ansLength = len(piles)/3
        ans = []
        piles.sort()
        
        for i in range(len(piles) - 2, -1, -2):
                if len(ans) < ansLength:
                    ans.append(piles[i])
                else:
                    break
        
        return sum(ans)
            
            