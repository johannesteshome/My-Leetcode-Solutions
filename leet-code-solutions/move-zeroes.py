class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        seeker = 1
        placeholder = 0

        while seeker < len(nums):
            if nums[placeholder] != 0:
                placeholder += 1
                seeker += 1
            elif nums[placeholder] == 0:
                if nums[seeker] == 0:
                    seeker += 1
                else:
                    nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
                    placeholder += 1
                    seeker += 1
        