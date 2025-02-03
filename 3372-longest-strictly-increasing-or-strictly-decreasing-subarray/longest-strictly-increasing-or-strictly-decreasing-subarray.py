class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasingLength = 1
        decreasingLength = 1

        length = 1

        # increasing subarray check
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                length += 1
            else:
                increasingLength = max(length, increasingLength)
                length = 1
        
        increasingLength = max(length, increasingLength)
        
        length = 1
        
        # decreasing subarray check
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                length += 1
            else: 
                decreasingLength = max(length, decreasingLength)
                length = 1
        
        decreasingLength = max(length, decreasingLength)
        
        # print(increasingLength, decreasingLength)
        
        return max(increasingLength, decreasingLength)
