class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        length = len(nums)
        for i in range(length):
            if(nums[index] == 0):
                del nums[index]
                nums.append(0)
            else:
                index = index + 1