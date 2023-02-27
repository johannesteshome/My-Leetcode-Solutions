class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1;
        postfix = 1;
        output = []
        
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
            
        for j in range(len(nums) - 1, -1, -1):
            output[j] = output[j] * postfix
            postfix = postfix * nums[j]
            
        return output
        