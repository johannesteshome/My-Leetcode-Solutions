class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        leftover = money - (prices[1] + prices[0])

        if leftover < 0:
            return money
        else:
            return leftover