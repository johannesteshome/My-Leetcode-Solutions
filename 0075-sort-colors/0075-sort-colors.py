class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        ones = []
        twos = []
        colors = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(nums[i])
            elif nums[i] == 1:
                ones.append(nums[i])
            elif nums[i] == 2:
                twos.append(nums[i])
        
        colors.extend(zeros)
        colors.extend(ones)
        colors.extend(twos)
        
        for i in range(len(nums)):
            nums[i] = colors[i]
            
        