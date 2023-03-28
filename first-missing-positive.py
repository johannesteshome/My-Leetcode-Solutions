class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
   
        i = 0

        while i < len(nums):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = -1
                i+=1
            else:
                index = nums[i] - 1
                if index != i:
                    if nums[index] == nums[i]:
                        nums[i] = -1
                    else:
                        nums[i], nums[index] = nums[index], nums[i]
                else:
                    i += 1
        
        for index, num in enumerate(nums):
            if num == -1:
                return index + 1

        return len(nums) +1