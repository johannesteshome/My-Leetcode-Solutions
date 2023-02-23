class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k-1
        avg = 0
        Max = float("-inf")
        
        if len(nums) == 1:
            return float(nums[0])
        
        Sum = sum(nums[left:right+1])
        avg = float(Sum/k)
        Max = max(Max, avg)
        right += 1
        left += 1
        while right < len(nums):
            Sum -= nums[left-1]
            Sum += nums[right]
            avg = float(Sum/k)
            Max = max(Max, avg)
            right += 1
            left += 1
            
            
            
        return Max
            
        