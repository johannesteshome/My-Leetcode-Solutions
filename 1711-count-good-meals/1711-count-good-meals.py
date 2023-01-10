class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        powersOfTwo = [2**i for i in range(22)]
    
        deliciousCount = Counter()
     
        answer = 0
        
        for d in deliciousness:
            for power in powersOfTwo:
                answer += deliciousCount[power-d]

            
            deliciousCount[d] += 1

    
        
        
        return answer  % ((10**9) + 7)
    
            