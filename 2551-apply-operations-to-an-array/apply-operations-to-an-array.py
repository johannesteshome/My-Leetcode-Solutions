class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] *= 0

        seeker = 1
        placeholder = 0

        while seeker < len(nums):
            if nums[placeholder] == 0:
                if nums[seeker] != 0:
                    nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
                    seeker += 1
                    placeholder += 1
                elif nums[seeker] == 0:
                    seeker += 1
            elif nums[placeholder] != 0:
                seeker += 1
                placeholder += 1
        
        return nums
