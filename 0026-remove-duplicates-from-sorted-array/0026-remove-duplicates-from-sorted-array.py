class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        read = 0
        count = 0
        
        while read < len(nums) - 1:
            if nums[read] == nums[read+1]:
                read += 1
            else:
                write+=1
                read+=1
                nums[write] = nums[read]
                
        
        print(nums)
                
        return write+1