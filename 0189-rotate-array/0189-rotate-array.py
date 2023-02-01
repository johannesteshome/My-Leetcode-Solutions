class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        toRemove = k%len(nums)
        nums[:toRemove] = reversed(nums[:toRemove])
        nums[toRemove:] = reversed(nums[toRemove:])
        