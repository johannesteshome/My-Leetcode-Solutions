class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        answer = numBottles

        while numBottles >= numExchange:
            drunk = numBottles // numExchange
            answer += drunk
            numBottles = drunk + (numBottles % numExchange)
        
        return answer