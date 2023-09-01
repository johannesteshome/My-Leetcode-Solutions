class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            count = 0
            num = i

            while num != 0:
                count += 1
                num = num - 2**(int(log2(num)))
            
            answer.append(count)
        
        return answer