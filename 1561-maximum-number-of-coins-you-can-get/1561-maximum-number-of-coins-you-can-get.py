class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort()
        
        for i in range(len(piles) - 1, len(piles)//3, -2):
                ans += piles[i-1]
        
        return ans
            
            