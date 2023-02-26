class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if len(nums) == 1:
            if nums[0] < target:
                return 0
            else: 
                return 1
        
        left = 0
        right = 0
        Min = float("inf")
        Sum = nums[left]
        if Sum < target:
            right += 1
            Sum += nums[right]
        else:
            Min = 1
        
        while left < len(nums):
            if Sum < target:
                if right == len(nums)-1:
                    break
                right += 1
                Sum += nums[right]
            else:
                Min = min(Min, right-left+1)
                left += 1
                Sum -= nums[left-1]
                
        if Min == float("inf"):
            return 0
        
        return Min