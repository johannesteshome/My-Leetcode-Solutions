class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        Max = max(nums)
        maxLength = float(-inf)
        length = 0

        for i in range(len(nums)):
            if nums[i] == Max:
                length += 1
            else:
                maxLength = max(length, maxLength)
                length = 0
        
        return max(maxLength, length)