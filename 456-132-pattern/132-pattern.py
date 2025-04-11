class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        monoStack = []
        currMin = nums[0]

        for i in range(1, len(nums)):

            while monoStack and monoStack[-1][0] <= nums[i]:
                monoStack.pop()
            
            if monoStack and nums[i] > monoStack[-1][1]:
                return True
            
            monoStack.append([nums[i], currMin])
            currMin = min(currMin, nums[i])
        
        return False
