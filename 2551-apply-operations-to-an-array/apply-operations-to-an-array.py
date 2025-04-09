class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        '''
        [1,4,0,2,0,0]

        '''

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        # move the zeroes after all the operations
        read = 0
        write = 0

        while read < len(nums):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp

                write += 1
            
            read += 1
        
        return nums