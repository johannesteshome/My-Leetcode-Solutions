class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)

        sum = 0
        start = 0
        maxAvg = float("-inf")
        
        for i in range(k):
            sum += nums[i]
        maxAvg = max(maxAvg, sum / k)
                
        for i in range(k, len(nums)):
            sum -= nums[start]
            sum += nums[i]

            start += 1

            maxAvg = max(maxAvg, sum / k)
        
        return maxAvg
            
