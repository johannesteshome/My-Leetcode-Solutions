class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        negativeCount = 0
    
        for num in nums:
            if num < 0:
                negativeCount += 1

        for i in range(32):
            count = 0
            for num in nums:
                if num < 0:
                    num = abs(num)
                if num & (1<<i) != 0:
                    count += 1
            print(count)
            if count % 3 != 0:
                answer |= (1<<i)
            
        return answer if negativeCount % 3 == 0 else -1 * answer