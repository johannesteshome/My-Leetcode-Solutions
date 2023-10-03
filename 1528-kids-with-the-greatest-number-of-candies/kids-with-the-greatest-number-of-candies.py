class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies[:i]+candies[i+1:]):
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
            
        