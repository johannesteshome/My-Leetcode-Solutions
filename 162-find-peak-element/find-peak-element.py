class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pre = []
        for i in range(1, len(nums)):
            val = abs(nums[i] - nums[i-1])
            if nums[i] > nums[i-1]:
                pre.append(val)
            else:
                pre.append(-val)
        
        for i in range(len(pre)):
            if pre[i] < 0:
                return i 
        return len(nums) - 1
            