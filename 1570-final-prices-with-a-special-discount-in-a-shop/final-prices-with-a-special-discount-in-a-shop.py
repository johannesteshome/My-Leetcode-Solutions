class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        i = 0

        while i < len(prices):
            # print(prices[i])
            discounted = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    discounted = True
                    answer.append(prices[i] - prices[j])
                    break
            if not discounted:
                answer.append(prices[i])
            i += 1
        
        return answer