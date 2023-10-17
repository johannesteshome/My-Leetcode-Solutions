class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0] = nums[0]

        for i in range(1, len(nums)):
            dp1[i] = max(dp1[i-1], nums[i]+dp2[i-1])
            dp2[i] = max(dp2[i-1], dp1[i-1] - nums[i])
        
        # print(dp1, dp2)
        return max(dp1[-1], dp2[-1])