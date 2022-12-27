class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        left1 = 0
        left2 = 1
        right = len(nums) - 1
        perimeters = [0]
        
        nums.sort()
        index = 1
        while(index <= (len(nums) - 2)):
            if(nums[-(index+2)] + nums[-(index+1)] > nums[-index]):
                return nums[-(index+2)] + nums[-(index+1)] + nums[-index]
            index += 1
        
        return 0