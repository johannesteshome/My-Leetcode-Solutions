class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = {}

        if len(nums) == 1:
            return nums[0]

        def dp(i, num, memo):
            n = len(num)
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i-1, num, memo), dp(i-2, num, memo) + num[i])
            return memo[i]
        
        return max(dp(len(nums) - 2, nums[1:], {}), dp(len(nums) - 2, nums[:-1], {}))