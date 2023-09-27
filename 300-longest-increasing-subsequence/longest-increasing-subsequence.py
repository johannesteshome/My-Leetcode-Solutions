class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(prev, curr):
            state = (prev)
            if state in memo:
                return memo[state]
            if curr < len(nums):
                if nums[prev] < nums[curr]:
                    memo[state] = max(1 + dp(curr, curr+1), dp(prev, curr+1))
                    return memo[state]
                else:
                    memo[state] = dp(prev, curr+1)
                    return memo[state]
            memo[state] = 1
            return memo[state]
        
        Max = 1

        for i in range(len(nums)-1):
            Max = max(Max, dp(i, i+1))
        
        
        return Max