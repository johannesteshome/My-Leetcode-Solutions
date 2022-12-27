class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        index = 0
        for i in range(len(nums)):
            if(nums[index]%2 != 0):
                nums.append(nums.pop(index))
            else:
                index += 1
                
        return nums