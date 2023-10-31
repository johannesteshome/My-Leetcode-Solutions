class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 1
        Max = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                Max = max(Max, profit)
            else:
                left = right
            right += 1
        
        return Max