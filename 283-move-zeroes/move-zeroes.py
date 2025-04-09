class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        [1,3,12,0,0]
                

        1. use read and write indices
        2. read index will iterate through the list and will look into zero
        3.

        """
        read = 0
        write = 0

        while read < len(nums):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp
            
                write += 1
            
            read += 1
        
        